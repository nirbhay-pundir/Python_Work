import os
import tkinter as tk
import tkinter.font as tkFont
import threading

def a():
    os.system("adb tcpip 5555")

def b():
    x1 = entry1.get()
    x2 = "adb connect {}:5555".format(x1)
    os.system(x2)

def c():
    tmp = threading.Thread(target=start, args=())
    tmp.start()

def start():
    os.system("scrcpy")

window=tk.Tk()
window.title('Wireless SCRCPY')
window.geometry("400x500+100+50")
fontStyle = tkFont.Font(family="Lucida Grande", size=20)
fontStyle2 = tkFont.Font(family="Lucida Grande", size=10)
fontStyle1 = tkFont.Font(family="Lucida Grande", size=15)
label=tk.Label(window,text="Steps To Follow:", font = fontStyle,height = 2)
label.pack(fill='x')
label=tk.Label(window,text="Step 1: Connect smartphone to machine\nusing data cable and enable usb debugging.", font = fontStyle1,height = 3)
label.pack()
label=tk.Label(window,text="Step 2: Click below button: ", font = fontStyle1)
label.pack(fill='x')
a = tk.Button(window,text="adb over tcp: 5555",command= a, font = fontStyle2,bg='#90CA83')
a.pack()
label=tk.Label(window,text="Step 3: Unplug Smartphone.", font = fontStyle1,height = 2)
label.pack(fill='x')
label=tk.Label(window,text="Step 4: Enter ip address below and\nclick below button: ", font = fontStyle1)
label.pack(fill='x')

entry1 = tk.Entry(window,font=fontStyle1,justify="center")
entry1.pack(fill='x')

b = tk.Button(window,text="Continue",command= b, font = fontStyle2,bg='#90CA83')
b.pack()

label=tk.Label(window,text="Step 2: Click below button: ", font = fontStyle1)
label.pack(fill='x')
c = tk.Button(window,text="Start Scrcpy",command= c, font = fontStyle2,bg='#90CA83')
c.pack()

window.mainloop()