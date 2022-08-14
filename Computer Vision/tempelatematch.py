import pyautogui as py
import time
import openpyxl
import cv2
import numpy as np

template = cv2.imread("icon.png")
template = cv2.cvtColor(template, cv2.COLOR_RGB2GRAY)
img = np.array(py.screenshot())
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
w, h = template.shape[::-1]
res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.9
loc = np.where(res >= threshold)
print(type(loc))
print(loc)
print(loc[0][0],loc[1][0])

# Draw a rectangle around the matched region.
for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)
#
# Show the final image with the matched area.
cv2.imwrite("imageResult.png",img)