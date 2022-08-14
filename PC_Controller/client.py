import socket
import pyautogui as py
import threading
import sys

py.FAILSAFE = False

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as c:
    def receiveData():
        global stop
        while True:
            try:
                data = c.recv(1024).decode()
                coordinates.append(data.split(','))
                print(coordinates)
            except ConnectionResetError:
                print("Disconnected...")
                stop = True
                break


    connected = False
    while not connected:
        try:
            IPaddr = input("Enter Ip Address: ")
            c.connect((IPaddr, 9999))
            print("Connected.......")
            connected = True
        except Exception:
            print("Device not found. Try Reconnecting.")

    coordinates = []
    stop = False

    tmp = threading.Thread(target=receiveData, args=())
    tmp.start()
    while True:
        if len(coordinates) != 0:
            xx = int(coordinates[0][0])
            yy = int(coordinates[0][1])
            print("Clicked at: ", xx, yy)
            py.moveTo(xx, yy, 0.2)
            py.click(xx, yy)
            coordinates.pop(0)
        if stop:
            tmp.join()
            sys.exit()
