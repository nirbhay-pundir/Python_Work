import time
import sys
import tkinter as tk
import threading
import socket
import tkinter.font as tkfont
import mouse
import pyautogui as py

stopped = False
slow = False
fast = True


# def clear_logs():
#     text.delete('1.0', tk.END)
#     #add_log("Logs have been cleared:")
#
# def add_log(log):
#     text.insert(tk.END,log + "\n")

def stop():
    global stopped
    print("Stopped....")
    stopped = True
    time.sleep(1)
    for worker in workers:
        worker.join()


def exit_():
    stop()
    s.close()
    sys.exit()


def sendData(x, y):
    try:
        c.send(bytes(str(x) + "," + str(y), 'utf-8'))
    except Exception as e:
        print("Disconnected start server again... ", e)


IPAddr = socket.gethostbyname(socket.gethostname())
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IPAddr, 9999))
s.listen(1)


def startServer():
    global c
    # add_log("Server Started.")
    print("Waiting for connection......")
    c, addr = s.accept()
    print("Connected with: ", addr)
    # clear_logs()
    # add_log("Connected.")

def start():
    global stopped, c, slow
    print("Started....")
    stopped = False
    # print("Slow = ",slow)
    while True:
        if mouse.is_pressed():
            sendData(py.position()[0], py.position()[1])
            time.sleep(0.1)

        elif stopped:
            break


workers = []
def start1():
    tmp = threading.Thread(target=start, args=())
    workers.append(tmp)
    tmp.start()


left = [100, 100]
right = [100, 100]


def selectLeft():
    global left
    while True:
        if mouse.is_pressed():
            left = py.position()
            print(left)
            break


def selectRight():
    global right
    while True:
        if mouse.is_pressed():
            right = py.position()
            print(right)
            break


window = tk.Tk()
window.title('PC Controller')
window.attributes('-topmost', 'true')
window.geometry("150x170+200+700")

fontStyle = tkfont.Font(family="Lucida Grande", size=15)
# text=tk.Text(window,height=13,background='black',fg='white')

labelIP = tk.Label(window, text=IPAddr, background='black', fg='white', font=fontStyle)
labelIP.pack(fill='x')

startServer = tk.Button(window, text="Start Server", command=startServer, bg='#A8F796', borderwidth=0,
                        activebackground='red')
startServer.pack(fill='x')

startWithButton = tk.Button(window, text="Start", command=start1, bg='#90CA83', borderwidth=0, activebackground='red')
startWithoutButton = tk.Button(window, text="Stop", command=stop, bg='#A8F796', borderwidth=0, activebackground='red')
buttonExit = tk.Button(window, text="Exit", command=exit_, bg='#90CA83', borderwidth=0, activebackground='red')
startWithButton.pack(fill='x')
startWithoutButton.pack(fill='x')
buttonExit.pack(fill='x')
# text.pack(fill='both')
window.mainloop()
