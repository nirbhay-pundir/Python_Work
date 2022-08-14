import cv2
import time

img = cv2.imread("images\\image1.png")
x = 291
y = 713
print(y)
for i in range(52,54):
    crop_img = img[round(y): round(y+44), x:x+44]
    y+=43
    print(round(y))
    cv2.imwrite(f"images\\{i}.png", crop_img)
    y += 34.6
    print(round(y))

# cv2.imwrite("images\\Image.png", img)
