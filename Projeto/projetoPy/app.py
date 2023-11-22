import cv2
import pytesseract
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
#img = cv2.imread("book.jpg")

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"



img = cv2.imread("bebeRuido.jpeg") 
img = cv2.resize(img, None, fx=0.75, fy=0.75) 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

img3 = cv2.imread("bebeRuido.jpeg") 
img3 = cv2.resize(img3, None, fx=0.75, fy=0.75) 
gray = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY) 

def showImageGrid(img, title):
    fig, axis = plt.subplots()
    imgMPLIB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    axis.imshow(imgMPLIB)
    axis.set_title(title)
    plt.show()

showImageGrid(img, "clarice.jpg")
showImageGrid(img, "bebeRuido.jpeg")


adaptive_threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 85, 11)

config = "--psm 4"
resultado = pytesseract.image_to_string(adaptive_threshold, config=config, lang='por')
#resultado = pytesseract.image_to_string(gray)

print(resultado)

cv2.imshow("gray", gray)
cv2.imshow("Img", img)
cv2.imshow("adaptive th", adaptive_threshold)
cv2.waitKey(0)



from matplotlib import pyplot as plt

def showSingleImage(img, title, size):
    fig, axis = plt.subplots(figsize = size)

    axis.imshow(img, 'gray')
    axis.set_title(title, fontdict = {'fontsize': 22, 'fontweight': 'medium'})
    plt.show()

def showImagenGrid(img, title):
    fig,axis = plt.subplots()
    imgMPLIB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    axis.imshow(imgMPLIB)
    axis.set_title(title)
    plt.show()

def plotTwoImageVertical():
    imgOriginal = cv2.imread("bebeRuido.jpeg")
    imgReplicate = cv2.copyMakeBorder(imgOriginal, 100, 100, 100, 100, cv2.BORDER_REPLICATE)

    imgsArray = [imgOriginal, imgReplicate]
    title = 'Imagem Original e Imagem com Borda Replicata'
    showMultipleImageGrid(imgsArray, title, 2, 0)

def plotTwoImageHorizontal():
    imgOriginal = cv2.imread("bebeRuido.jpeg")
    imgReplicate = cv2.copyMakeBorder(imgOriginal, 200, 100, 50, 25, cv2.BORDER_REPLICATE)

    imgsArray = [imgOriginal, imgReplicate]
    title = 'Imagem Original e Imagem com Borda Replicata'
    showMultipleImageGrid(imgsArray, title, 2, 1)

def main():
    plotTwoImageHorizontal()

if __name__ == "__main__":
    main()

def showImage(img):
    imgMPLIB = cv2.cvtcolor(img,cv2.COLOR_BGR2RGB)

def showMultipleImageGrid(imgsArray, titlesArray, size, x, y):
    if(x < 1 or y < 1):
        print("ERRO: X e Y não podem ser zero ou abaixo de zero!")
        return
    elif(x == 1 and y == 1):
        showSingleImage(imgsArray, titlesArray)
    elif(x == 1):
        fig, axis = plt.subplots(y, figsize = size)
        yId = 0
        for img in imgsArray:
            axis[yId].imshow(img, 'gray')
            axis[yId].set_anchor('NW')
            axis[yId].set_title(titlesArray[yId], fontdict = {'fontsize': 18, 'fontweight': 'medium'}, pad = 10)

            yId += 1
    elif(y == 1):
        fig, axis = plt.subplots(1, x, figsize = size)
        fig.suptitle(titlesArray)
        xId = 0
        for img in imgsArray:
            axis[xId].imshow(img, 'gray')
            axis[xId].set_anchor('NW')
            axis[xId].set_title(titlesArray[xId], fontdict = {'fontsize': 18, 'fontweight': 'medium'}, pad = 10)

            xId += 1
    else:
        fig, axis = plt.subplots(y, x, figsize = size)
        xId, yId, titleId = 0, 0, 0
        for img in imgsArray:
            axis[yId, xId].set_title(titlesArray[titleId], fontdict = {'fontsize': 18, 'fontweight': 'medium'}, pad = 10)
            axis[yId, xId].set_anchor('NW')
            axis[yId, xId].imshow(img, 'gray')
            if(len(titlesArray[titleId]) == 0):
                axis[yId, xId].axis('off')

            titleId += 1
            xId += 1
            if xId == x:
                xId = 0
                yId += 1
    plt.show()

svbr_img = cv2.imread("bebeRuido.jpeg")
svbr_img = cv2.cvtColor(svbr_img, cv2.COLOR_BGR2RGB)
showSingleImage(svbr_img, "SVBR", (5, 7))



#FILTRO LAPLACIANO

import time

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
#FILTRO DE BORRA IMAGEM

# Apresentação de filtros
from PIL import Image, ImageFilter
from math import sqrt
import os
from utils import show_vertical, show_horizontal, in_file, out_file


# IMPC06 | "Borrando uma Imagem em Python": https://youtu.be/IgQfpMPblR0
def show_box_blur(filename, r=1):
    '''Aplica um filtro BoxBlur à imagem, exibe e salva o resultado'''

    original = Image.open(in_file(filename))
    filtered = original.filter(ImageFilter.BoxBlur(r))

    #Mostrar as imagens lado a lado
    show_horizontal(original, filtered)
    filtered.save(
        out_file(
            '{}_boxblur_{}.jpg'.format(filename[:filename.index('.')], r)
        )
    )

# IMPC07 | "DETECTANDO ARESTAS na Imagem com Filtro Sobel": https://youtu.be/uHT4qDzq1bY
def show_edges(filename, direction='x',offset=0):
    '''Aplica um filtro Sobel à imagem, exibe e salva o resultado'''

    original = Image.open(in_file(filename)).convert('L')
    XSOBEL = ImageFilter.Kernel((3, 3),
                                [-1, 0, 1,
                                -2, 0, 2,
                                -1, 0, 1],
                                1, 
                                offset)
    YSOBEL = ImageFilter.Kernel((3, 3),
                                [-1, -2, -1,
                                0, 0, 0,
                                1, 2, 1],
                                1,
                                offset)
    if direction == 'x':
        filtered = original.filter(XSOBEL)
    elif direction == 'y':
        filtered = original.filter(YSOBEL)
    else:
        vsobel = original.filter(XSOBEL)
        hsobel = original.filter(YSOBEL)
        w, h = original.size
        filtered = Image.new('L', (w, h))

        for i in range(w):
            for j in range(h):
                value = sqrt(
                    vsobel.getpixel((i, j))**2 + hsobel.getpixel((i, j))**2
                )
                value = int(min(value, 255))
                filtered.putpixel((i, j), value)

    # Mostrar as imagens lado a lado
    show_horizontal(original, filtered)
    filtered.save(
        out_file(
            '{}_{}sobel_{}.jpg'.format(
                                    filename[:filename.index('.')], 
                                    direction,
                                    offset)
        )
    )


if __name__ == "__main__":
    # Experimente outras imagens e tamanhos de filtros
    show_box_blur('email.jpg', 4)
    show_edges('email.jpg', 'a', 0)
"""


#Filtro de Mediana

bebeRuido = cv2.imread("bebeRuido.jpeg")
median_img = cv2.medianBlur(bebeRuido.jpeg, 5)

imgsArray = [bebeRuido.jpeg, median_img]
titlesArray = ['Original', 'Median Filter']
showMultipleImageGrid(imgsArray, titlesArray, (12, 8), 2, 1)