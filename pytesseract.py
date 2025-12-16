import pytesseract
from PIL import Image, ImageEnhance
import PIL.ImageOps
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
result = pytesseract.image_to_string("1.jpg")
print(result)
