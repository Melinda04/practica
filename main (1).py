import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

print(pytesseract.image_to_string(r'C:\Users\Gabriel\PycharmProjects\pythonProject5\citat.jpg'))