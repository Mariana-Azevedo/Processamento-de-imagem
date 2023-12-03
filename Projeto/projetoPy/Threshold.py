import numpy as np
import cv2
import pytesseract
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

def showImage(img):
    imgMPLIB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(imgMPLIB)
    plt.show()

def showMultipleImageGrid(imgsArray, titlesArray, x, y):
    if(x < 1 or y < 1):
        print("ERRO: X e Y não podem ser zero ou abaixo de zero!")
        return
    elif(x == 1 and y == 1):
        showImageGrid(imgsArray, titlesArray)
    elif(x == 1):
        fig, axis = plt.subplots(y)
        fig.suptitle(titlesArray)
        yId = 0
        for img in imgsArray:
            imgMPLIB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            axis[yId].imshow(imgMPLIB)

            yId += 1
    elif(y == 1):
        fig, axis = plt.subplots(1, x)
        fig.suptitle(titlesArray)
        xId = 0
        for img in imgsArray:
            imgMPLIB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            axis[xId].imshow(imgMPLIB)

            xId += 1
    else:
        fig, axis = plt.subplots(y, x)
        xId, yId, titleId = 0, 0, 0
        for img in imgsArray:
            imgMPLIB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            axis[yId, xId].set_title(titlesArray[titleId])
            axis[yId, xId].imshow(imgMPLIB)
            if(len(titlesArray[titleId]) == 0):
                axis[yId, xId].axis('off')

            titleId += 1
            xId += 1
            if xId == x:
                xId = 0
                yId += 1

        fig.tight_layout(pad=0.5)
    plt.show()

def plotSingleImage():
    #criando grid com a imagem original apenas
    imgOriginal = cv2.imread("Projeto/clarice.jpg")
    showImageGrid(imgOriginal, "Foto da Ada")

    imgOriginal = cv2.imread("Projeto/clarice.jpg")
    imgReplicate = cv2.copyMakeBorder(imgOriginal, 100, 100, 100, 100, cv2.BORDER_REPLICATE)
    imgReflect = cv2.copyMakeBorder(imgOriginal, 100, 100, 100, 100, cv2.BORDER_REFLECT)
    imgReflect101 = cv2.copyMakeBorder(imgOriginal, 100, 100, 100, 100, cv2.BORDER_REFLECT_101)
    imgWrap = cv2.copyMakeBorder(imgOriginal, 100, 100, 100, 100, cv2.BORDER_WRAP)

    BLUE = [255, 0, 0]
    imgConstant = cv2.copyMakeBorder(imgOriginal, 100, 100, 100, 100, cv2.BORDER_CONSTANT, value = BLUE)

    #criando grid com 6 imagens, a segunda com borda replicada e a terceira e quarta com borda de espelho
    #constant insere uma moldura e wrap só olhando pra entender =)
    imgsArray = [imgOriginal, imgReplicate, imgReflect, imgReflect101, imgConstant, imgWrap]
    titlesArray = ['Original', 'Borda Replicada', 'Borda de Espelho', 'Borda de Espelho 2', 'Moldura', 'Efeito Wrap']
    showMultipleImageGrid(imgsArray, titlesArray, 3, 2)

def showImageGrid(img, title):
    fig, axis = plt.subplots()
    imgMPLIB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    axis.imshow(imgMPLIB)
    axis.set_title(title)
    plt.show()

def plotTwoImageHorizontal():

    imgOriginal = cv2.imread("Projeto/clarice.jpg")
    gray = cv2.cvtColor(imgOriginal, cv2.COLOR_BGR2GRAY) 
    imgReplicate = cv2.copyMakeBorder(imgOriginal, 100, 100, 100, 100, cv2.BORDER_REPLICATE)
    imgReplicate = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 85, 11)

    config = "--psm 4"
    resultado = pytesseract.image_to_string(imgReplicate, config=config, lang='por')
    #criando grid com 2 imagens, a segunda com borda replicada
    imgsArray = [imgOriginal, imgReplicate]
    title = 'Imagem Original e Imagem com Borda Replicada'
    showMultipleImageGrid(imgsArray, title, 2, 1)

def main():
    plotTwoImageHorizontal()
    

if __name__ == "__main__":
    main()

def showSingleImage(img, title, size):
    fig, axis = plt.subplots(figsize = size)

    axis.imshow(img, 'gray')
    axis.set_title(title, fontdict = {'fontsize': 22, 'fontweight': 'medium'})
    plt.show()

svbr_img = cv2.imread("clarice.jpg")
svbr_img = cv2.cvtColor(svbr_img, cv2.COLOR_BGR2RGB)
showSingleImage(svbr_img, "SVBR", (2, 1))
