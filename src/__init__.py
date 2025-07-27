from PIL import Image, ImageFilter

def preprocess_image(image_path):
    """
    Applies preprocessing to an image to improve OCR accuracy.
    """
    img = Image.open(image_path)
    # Convert to grayscale
    img = img.convert('L')
    # Apply a filter to sharpen the image
    img = img.filter(ImageFilter.SHARPEN)
    preprocessed_path = "preprocessed_" + image_path
    img.save(preprocessed_path)
    return preprocessed_path