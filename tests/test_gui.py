import unittest
import sys
from PyQt5.QtWidgets import QApplication
from src.gui import ScreenshotWindow

class TestGui(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = QApplication(sys.argv)

    def test_screenshot_window_creation(self):
        """Test if the screenshot window is created successfully."""
        window = ScreenshotWindow()
        self.assertIsInstance(window, ScreenshotWindow)

    # Further GUI tests would require a more complex setup to simulate user interactions.

if __name__ == '__main__':
    unittest.main()