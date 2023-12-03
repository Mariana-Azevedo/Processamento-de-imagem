import numpy as np
import cv2
import pytesseract
import matplotlib.pyplot as plt
import random
from matplotlib import pyplot as plt
from PIL import Image
import math


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

def showImage(img):
    imgMPLIB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(imgMPLIB)
    plt.show()

def showSingleImage(img, title, size):
    fig, axis = plt.subplots(figsize = size)

    axis.imshow(img, 'gray')
    axis.set_title(title, fontdict = {'fontsize': 22, 'fontweight': 'medium'})
    plt.show()
    
def showMultipleImages(imgsArray, titlesArray, size, x, y):
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

def moire(source, target, angle, distance, offsetx = 2, offsety = 2):

    #imagem de entrada
    img = Image.open(source)
    pm = img.load()
    # imagem de saída (usando a mesma para gerar sobreposição)
    imgout = Image.open(source)
    pmout = imgout.load()

    # valores para as transformações    
    cosseno = math.cos(angle)
    seno = math.sin(angle)
    # distância em cada eixo
    dx = distance * cosseno 
    dy = distance * seno

    for x in range(0, img.size[0], offsetx):
        for y in range(0, img.size[1], offsety):
            # calcula coordenada transformada (rotação + deslocamento)
            x2, y2 = dx + math.floor(x * cosseno - y * seno), dy + math.floor(x * seno + y * cosseno)
            # ajusta valores fora da imagem (como se a mesma repetisse infinitamente)
            if x2 < 0:
                x2 = img.size[0] + x2
            elif x2 >= img.size[0]:
                x2 = x2 - img.size[0]
            if y2 < 0:
                y2 = img.size[1] + y2
            elif y2 >= img.size[1]:
                y2 = y2 - img.size[1]
            # desenha ponto transformado 
            pmout[x, y] = pm[x2, y2] 

    # salva a imagem
    imgout.save(target)

def showImageGrid(img, title):
    fig, axis = plt.subplots()
    imgMPLIB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    axis.imshow(imgMPLIB)
    axis.set_title(title)
    plt.show()

def plotTwoImageHorizontal(img):
    
    imgOriginal = cv2.imread(img)
    imgReplicate = cv2.medianBlur(imgOriginal, 5)

    imgsArray = [imgOriginal, imgReplicate]
    titlesArray = ['Original', 'Filtro de Mediana']
    showMultipleImages(imgsArray, titlesArray, (12, 8), 2, 1)

    config = "--psm 4"
    resultado = pytesseract.image_to_string(imgReplicate, config=config)
    #criando grid com 2 imagens, a segunda com borda replicada
    imgsArray = [imgOriginal, imgReplicate]
    title = 'Imagem Original e Imagem com Adaptive Threshold'
    showMultipleImages(imgsArray, title, 2, 1)

def main():
    img_path = "Projeto/phone.jpg"
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    #img_with_noise = add_noise(img)
    
    # Salva a imagem com ruído
    #cv2.imwrite('Projeto/phone_with_noise.jpg', img_with_noise)

    # Passa o caminho da imagem para plotTwoImageHorizontal
    img = moire(r'Pojeto\pixar.jpg', r'linhas-output-1.png', math.pi / 4, 0, 1, 1)
    #plotTwoImageHorizontal(img_path)

    plotTwoImageHorizontal(img)
    

if __name__ == "__main__":
    main()

def showSingleImage(img, title, size):
    fig, axis = plt.subplots(figsize = size)

    axis.imshow(img, 'gray')
    axis.set_title(title, fontdict = {'fontsize': 22, 'fontweight': 'medium'})
    plt.show()