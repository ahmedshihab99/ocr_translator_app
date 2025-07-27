import pytesseract
from PIL import Image
from utils.config import TESSERACT_CMD
import logging

pytesseract.pytesseract.tesseract_cmd = TESSERACT_CMD

def ocr_image(image_path, lang='eng'):
    """
    Performs OCR on an image file.
    """
    try:
        text = pytesseract.image_to_string(Image.open(image_path), lang=lang)
        logging.info(f"OCR successful for {image_path}")
        print(f"OCR Result: {text.strip()}")
        return text.strip()
    except Exception as e:
        logging.error(f"Error during OCR: {e}")
        print(f"Error during OCR: {e}")
        return ""