import tkinter as tk
import pytesseract
import cv2
import mss
import time
import re
import numpy as np
import threading
import sys

# 691 849
sct = mss.mss()
left = 267
top = 432
right = 691
bottom = 849
mon = {"top": top, "left": left, "width": right - left, "height": bottom - top}
left1 = 621
top1 = 336
right1 = 680
bottom1 = 370
mon1 = {"top": top1, "left": left1, "width": right1 - left1, "height": bottom1 - top1}
list = []
workers = []
stopped = False


def stop():
    global stopped
    stopped = True
    time.sleep(1)
    for worker in workers:
        worker.join()


def exit():
    stop()
    sys.exit()


def replace_chars(text):
    list_of_numbers = re.findall(r'\d+', text)
    result_number = ''.join(list_of_numbers)
    if '0' not in result_number and len(result_number) == 1:
        result_number += str(1)
    return result_number


def createArray():
    global list
    list = []
    image1 = np.array(sct.grab(mon))
    # image = cv2.resize(image,(400,400),interpolation=cv2.INTER_LINEAR)
    image = cv2.cvtColor(image1, cv2.COLOR_RGBA2GRAY)
    blur = cv2.bilateralFilter(image,9,75,75)
    # blur = cv2.GaussianBlur(image, (5, 5), 0)
    cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    hsv = cv2.cvtColor(image1,cv2.COLOR_RGB2HSV)
    # lower_blue = np.array([220, 210, 225])
    # upper_blue = np.array([255, 255, 255])
    lower_blue = np.array([120, 58, 35])
    upper_blue = np.array([200, 202, 221])
    mask = cv2.bitwise_not(cv2.inRange(hsv, lower_blue, upper_blue))
    image = cv2.bitwise_and(image, image, mask=mask)
    cv2.imshow('img',image)

    leftTemp = 0
    topTemp = 0
    for i in range(5):
        a = []
        leftTemp = 0
        for j in range(5):
            tempImg = image[topTemp + 5:topTemp + 72, :]
            tempImg = tempImg[:, leftTemp:leftTemp + 73]
            leftTemp += 86
            print(replace_chars(pytesseract.image_to_string(tempImg, config='--psm 6')))
            a.append(replace_chars(pytesseract.image_to_string(tempImg, config='--psm 6')))
            cv2.imshow('Image', tempImg)
            key = cv2.waitKey(1)
            if key == 27:
                break
            time.sleep(0.1)
        topTemp += 85
        list.append(a)
    for row in list:
        print(row)


def threadStart():
    global stopped, c
    stopped = False
    while True:
        img = np.array(sct.grab(mon1))



def start():
    tmp = threading.Thread(target=start, args=())
    workers.append(tmp)
    tmp.start()


window = tk.Tk()
window.title("Tambola Bot")
window.attributes('-topmost', 'true')
window.geometry("200x200+1500+700")

createArray = tk.Button(window, text="Create Array", command=createArray, background='#90CA83')
createArray.pack(fill='x')
startButton = tk.Button(window, text="Start", command=start, background='#90CA83')
startButton.pack(fill='x')
stopButton = tk.Button(window, text="Stop", command=stop, background='#90CA83')
stopButton.pack(fill='x')
exitButton = tk.Button(window, text="Exit", command=exit, background='#90CA83')
exitButton.pack(fill='x')
window.mainloop()
