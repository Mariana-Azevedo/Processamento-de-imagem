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

def showMultipleImages(imgsArray, titlesArray, size, x, y, mincolor=0, maxcolor=255):
    if(x < 1 or y < 1):
        print("ERRO: X e Y não podem ser zero ou abaixo de zero!")
        return
    elif(x == 1 and y == 1):
        showSingleImage(imgsArray, titlesArray)
    elif(x == 1):
        fig, axis = plt.subplots(y, figsize = size)
        yId = 0
        for img in imgsArray:
            axis[yId].imshow(img, cmap='gray', vmin=mincolor, vmax=maxcolor)
            axis[yId].set_anchor('NW')
            axis[yId].set_title(titlesArray[yId], fontdict = {'fontsize': 18, 'fontweight': 'medium'}, pad = 10)

            yId += 1
    elif(y == 1):
        fig, axis = plt.subplots(1, x, figsize = size)
        fig.suptitle(titlesArray)
        xId = 0
        for img in imgsArray:
            axis[xId].imshow(img, cmap='gray', vmin=mincolor, vmax=maxcolor)
            axis[xId].set_anchor('NW')
            axis[xId].set_title(titlesArray[xId], fontdict = {'fontsize': 18, 'fontweight': 'medium'}, pad = 10)

            xId += 1
    else:
        fig, axis = plt.subplots(y, x, figsize = size)
        xId, yId, titleId = 0, 0, 0
        for img in imgsArray:
            axis[yId, xId].set_title(titlesArray[titleId], fontdict = {'fontsize': 18, 'fontweight': 'medium'}, pad = 10)
            axis[yId, xId].set_anchor('NW')
            axis[yId, xId].imshow(img, cmap='gray', vmin=mincolor, vmax=maxcolor)
            if(len(titlesArray[titleId]) == 0):
                axis[yId, xId].axis('off')

            titleId += 1
            xId += 1
            if xId == x:
                xId = 0
                yId += 1
    plt.show()

def plotSingleImage():
    #criando grid com a imagem original apenas
    #imgOriginal = cv2.imread("Projeto/palavras.jpg")
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
    showMultipleImages(imgsArray, titlesArray, 3, 2)

def showImageGrid(img, title):
    fig, axis = plt.subplots()
    imgMPLIB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    axis.imshow(imgMPLIB)
    axis.set_title(title)
    plt.show()

def plotThreeImages():
    img_j_original = cv2.imread("Projeto/trio.jpg", 0)

    #mesma imagem com erosão
    kernel = np.ones((3,3),np.uint8)
    erosao =  cv2.erode(img_j_original, kernel, iterations=1)

    #imagem anterior com dilatação aplicada
    dilatacao =  cv2.dilate(erosao, kernel, iterations=1)

    imgsArray = [img_j_original, erosao, dilatacao]
    titlesArray = ['Imagem Original', 'Erosão', 'Dilatação']
    showMultipleImages(imgsArray, titlesArray, (10, 6), 3, 1)
    
    config = "--psm 4"
    resultado = pytesseract.image_to_string(dilatacao, config=config, lang='por')
    #resultado = pytesseract.image_to_string(gray)

    print(resultado)

    #criando grid com 3 imagens, a segunda com borda replicada e a terceira com borda de espelho
    #a ultima imagem é transparente
    """imgsArray = [imgOriginal, imgReplicate, imgReflect, imgTransparent]
    titlesArray = ['Original', 'Borda Replicada', 'Borda de Espelho', '']
    showMultipleImageGrid(imgsArray, titlesArray, 2, 2)"""

def plotTwoImageHorizontal():

    """imgOriginal = cv2.imread("Projeto/palavras.jpg")
    gray = cv2.cvtColor(imgOriginal, cv2.COLOR_BGR2GRAY) 
    imgReplicate = cv2.copyMakeBorder(imgOriginal, 100, 100, 100, 100, cv2.BORDER_REPLICATE)
    imgReplicate = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 85, 11)"""

    #imagem original
    img_j_original = cv2.imread("Projeto/erosao.jpg", 0)

    #mesma imagem com erosão
    kernel = np.ones((3,3),np.uint8)
    erosion =  cv2.erode(img_j_original, kernel, iterations=1)

    #imagem anterior com dilatação aplicada
    dilation =  cv2.dilate(erosion, kernel, iterations=1)

    imgsArray = [img_j_original, erosion, dilation]
    titlesArray = ['Original', 'Erosion', 'Dilation']
    showMultipleImages(imgsArray, titlesArray, (10, 6), 3, 1)

    """config = "--psm 4"
    resultado = pytesseract.image_to_string(imgReplicate, config=config, lang='por')
    #criando grid com 2 imagens, a segunda com borda replicada
    imgsArray = [imgOriginal, imgReplicate]
    title = 'Imagem Original e Imagem com Borda Replicada'
    showMultipleImageGrid(imgsArray, title, 2, 1)"""

#threshold, img_thresh = cv2.threshold(img_moedas, 127, 255, cv2.THRESH_BINARY_INV)
#showSingleImage(img_thresh, "Threshold Image", (7, 7))

def main():
    plotThreeImages()
    

if __name__ == "__main__":
    main()

def showSingleImage(img, title, size):
    fig, axis = plt.subplots(figsize = size)

    axis.imshow(img, 'gray')
    axis.set_title(title, fontdict = {'fontsize': 22, 'fontweight': 'medium'})
    plt.show()

"""svbr_img = cv2.imread("Projeto/trio.jpg")
svbr_img = cv2.cvtColor(svbr_img, cv2.COLOR_BGR2RGB)
showSingleImage(svbr_img, "SVBR", (2, 1))"""
