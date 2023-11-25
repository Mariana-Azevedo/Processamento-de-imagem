import cv2
import numpy as np
import pytesseract
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
import pytesseract as pt

pt.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

img = cv2.imread('Projeto\phone.jpg')
boxes = pt.image_to_boxes(img, lang='por')
imH, imW,_ = img.shape



for b in boxes.splitlines():
    b = b.split(' ')
    letra,x,y,w,h = b[0], int (b[1]), int(b[2]), int(b[3]), int(b[4])
    cv2.rectangle(img,(x,imH-y),(w,imH-h),(0,0,255))
    cv2.putText(img,letra,(x,imH-y+25), cv2.FONT_HERSHEY_SIMPLEX,1, (0,0,2555), 2)
    #print(b)

cv2.imshow('Imagem', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
