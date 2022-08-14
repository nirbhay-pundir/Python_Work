import cv2
import numpy as np
import mss

sct = mss.mss()
top = 730
left = 350
bottom = 735
right = 355
mon1 = {"top": top, "left": left, "width": right-left, "height": bottom-top}
left += 110
right += 110
mon2 = {"top": top, "left": left, "width": right-left, "height": bottom-top}
left += 110
right += 110
mon3 = {"top": top, "left": left, "width": right-left, "height": bottom-top}
left += 110
right += 110
mon4 = {"top": top, "left": left, "width": right-left, "height": bottom-top}

while True:
    frame1 = np.array(sct.grab(mon3))
    # frame = cv2.imread('example.png')
    frame = cv2.cvtColor(frame1, cv2.COLOR_RGBA2RGB)
    hsv = frame

    lower_blue = np.array([0, 0, 0])
    upper_blue = np.array([15, 15, 15])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("result", result)

    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()