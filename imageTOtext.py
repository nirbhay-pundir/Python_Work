import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = 'Tesseract-OCR\\tesseract.exe'
img=cv2.imread('0006.jpg')
print(pytesseract.image_to_string(img))