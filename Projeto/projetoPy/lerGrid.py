import cv2
import pytesseract as pt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt

pt.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

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
        for img, title in zip(imgsArray, titlesArray):
            imgMPLIB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            axis[yId, xId].set_title(title)
            axis[yId, xId].imshow(imgMPLIB)
            if(len(title) == 0):
                axis[yId, xId].axis('off')

            titleId += 1
            xId += 1
            if xId == x:
                xId = 0
                yId += 1

        fig.tight_layout(pad=0.5)
    plt.show()

def plotTwoImageHorizontal():

    imgOriginal = cv2.imread("Projeto/palavras.jpg")
    gray = cv2.cvtColor(imgOriginal, cv2.COLOR_BGR2GRAY) 
    imgReplicate = cv2.copyMakeBorder(imgOriginal, 100, 100, 100, 100, cv2.BORDER_REPLICATE)
    imgReplicate = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 85, 11)

    config = "--psm 4"
    resultado = pt.image_to_string(imgReplicate, config=config, lang='por')
    # criando grid com 2 imagens, a segunda com borda replicada
    imgsArray = [imgOriginal, imgReplicate]
    titlesArray = ['Imagem Original', 'Imagem com Borda Replicada\nTexto Reconhecido: ' + resultado]
    showMultipleImageGrid(imgsArray, titlesArray, 2, 1)

def main():
    plotTwoImageHorizontal()

if __name__ == "__main__":
    main()

def showImageGrid(img, title):
    fig, axis = plt.subplots()
    imgMPLIB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    axis.imshow(imgMPLIB)
    axis.set_title(title)
    plt.show()

def plotSegmentedCharacters():

    img = cv2.imread('Projeto\palavras.jpg')
    boxes = pt.image_to_boxes(img, lang='por')
    imH, imW,_ = img.shape

    for b in boxes.splitlines():
        b = b.split(' ')
        letra, x, y, w, h = b[0], int(b[1]), int(b[2]), int(b[3]), int(b[4])
        cv2.rectangle(img, (x, imH - y), (w, imH - h), (0, 0, 255))
        cv2.putText(img, letra, (x, imH - y + 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 2555), 2)

    cv2.imshow('Imagem', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    plotSegmentedCharacters()
