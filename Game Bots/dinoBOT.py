import cv2
import mss
import numpy as np
import pyautogui


left = 420
top = 315
right = 470
bottom = 339
mon = {"top": top, "left": left, "width": right - left, "height": bottom - top}
sct = mss.mss()

count = 1

while True:
    img = np.array(sct.grab(mon))
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gray = cv2.bitwise_not(gray)
    a = gray.sum()
    if a != 9600:
        pyautogui.press("space")
    if count%700==0:
        left +=5
        right +=5
        print(left,",",right)
    count+=1
    # if a!= 10752:
    # print(a)
    # cv2.imshow("img",img)
    # key = cv2.waitKey(1)
    # if key==27:
    #     break