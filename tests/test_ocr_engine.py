import unittest
from src.ocr_engine import ocr_image
from PIL import Image, ImageDraw, ImageFont

class TestOcrEngine(unittest.TestCase):

    def setUp(self):
        """Create a dummy image for testing."""
        self.image_path = "test_image.png"
        img = Image.new('RGB', (400, 100), color = (255, 255, 255))
        d = ImageDraw.Draw(img)
        try:
            font = ImageFont.truetype("arial.ttf", 40)
        except IOError:
            font = ImageFont.load_default()
        d.text((10,10), "This is a test", fill=(0,0,0), font=font)
        img.save(self.image_path)

    def test_ocr_image(self):
        """Test the OCR functionality."""
        extracted_text = ocr_image(self.image_path)
        self.assertIn("This is a test", extracted_text)

    def tearDown(self):
        """Remove the dummy image."""
        import os
        os.remove(self.image_path)

if __name__ == '__main__':
    unittest.main()