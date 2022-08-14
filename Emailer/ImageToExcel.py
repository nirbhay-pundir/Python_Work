import pytesseract
import cv2
import openpyxl

pytesseract.pytesseract.tesseract_cmd = "tesseract"
img = cv2.imread("screenshot.png")
text = pytesseract.image_to_string(img)
wb = openpyxl.load_workbook("U1LoginEmails.xlsx")
sheet = wb['Sheet1']
text = text.split("\n")
i = 1
for str in text:
    if "@gmail.com" in str:
        print(str,end =" ")
        sheet.cell(i, 1, value=str)
        wb.save("U1LoginEmails.xlsx")
        i += 1
