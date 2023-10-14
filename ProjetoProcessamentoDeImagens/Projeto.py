import pytesseract
import cv2

#passo 1: ler a imagem
imagem = cv2.imread("email.jpg")

caminho= r"C:\Program Files\Tesseract-OCR"
#passo 2: pedir para o tesseract extrair o texto da imagem
pytesseract.pytesseract.tesseract_cmd = caminho + r"\tesseract.exe"
texto = pytesseract.image_to_string(imagem)


print(texto)