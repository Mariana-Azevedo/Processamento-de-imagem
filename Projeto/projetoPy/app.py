import cv2
import pytesseract

#img = cv2.imread("book.jpg")

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

img = cv2.imread("clarice.jpg") 
img = cv2.resize(img, None, fx=0.75, fy=0.75) 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 


adaptive_threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 85, 11)

config = "--psm 4"
resultado = pytesseract.image_to_string(adaptive_threshold, config=config)
#resultado = pytesseract.image_to_string(gray)

print(resultado)

cv2.imshow("gray", gray)
cv2.imshow("Img", img)
cv2.imshow("adaptive th", adaptive_threshold)
cv2.waitKey(0)