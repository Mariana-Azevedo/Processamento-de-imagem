import cv2
import pytesseract
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import pyplot as plt
#img = cv2.imread("book.jpg")

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

img = cv2.imread("Projeto\ImagemRaiox.jpg") 
img = cv2.resize(img, None, fx=0.75, fy=0.75) 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 



adaptive_threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 85, 11)

config = "--psm 4"
resultado = pytesseract.image_to_string(adaptive_threshold, config=config, lang='por')
#resultado = pytesseract.image_to_string(gray)

print(resultado)

cv2.imshow("gray", gray)
cv2.imshow("Img", img)
cv2.imshow("adaptive th", adaptive_threshold)
cv2.waitKey(0)



#FILTRO LAPLACIANO

"""import time

ESCAPE_KEY_ASCII = 27

def onChange(value):
    pass

#imagem carregada e sua cópia
img2 = cv2.imread("book.jpg") 
img2 = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)
img2 = cv2.GaussianBlur(img2, (3, 3), 3, 3)
copyimg = img.copy()

#cria janela gráfica para inserir a imagem
windowTitle = "Canny Edge Detector"
cv2.namedWindow(windowTitle)

#cria trackbar
cv2.createTrackbar("limiar_min", windowTitle, 0, 300, onChange)
cv2.createTrackbar("limiar_max", windowTitle, 0, 300, onChange)

before_min_thresh = 0
update_min_thresh = False
before_max_thresh = 0
update_max_thresh = False
counter_time = 0

while True:
    current_min_thresh = cv2.getTrackbarPos("limiar_min", windowTitle)
    
    #valor de limiar do trackbar foi alterado pelo usuário? (sim)
    if before_min_thresh != current_min_thresh:
        update_min_thresh = True
        counter_time = time.time()
        before_min_thresh = current_min_thresh
        
    #se tiver passado 1 segundo desde que o usuário mexeu em algum trackbar
    if time.time() - counter_time > 1:
        #se tiver sido marcado que é pra atualizar o filtro canny
        if update_min_thresh == True:
            
            #fazemos uma cópia da imagem original
            copyimg = cv2.Canny(img2, current_min_thresh, current_max_thresh)
            update_min_thresh = False
            
    current_max_thresh = cv2.getTrackbarPos("limiar_max", windowTitle)
    
    #valor de limiar do trackbar foi alterado pelo usuário? (sim)
    if before_max_thresh != current_max_thresh:
        update_max_thresh = True
        counter_time = time.time()
        before_max_thresh = current_max_thresh
        
    #se tiver passado 1 segundo desde que o usuário mexeu em algum trackbar
    if time.time() - counter_time > 1:
        #se tiver sido marcado que é pra atualizar o filtro canny
        if update_max_thresh == True:
            
            #fazemos uma cópia da imagem original
            copyimg = cv2.Canny(img2, current_min_thresh, current_max_thresh)
            update_max_thresh = False
        
   # cv2.imshow(windowTitle, copyimg)
    
    keyPressed = cv2.waitKey(1) & 0xFF
    if keyPressed == ESCAPE_KEY_ASCII:
        break
        
cv2.destroyAllWindows()

"""

