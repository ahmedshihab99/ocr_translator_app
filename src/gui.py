from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt, QRect, QTimer
from PyQt5.QtGui import QPainter, QPen, QColor, QGuiApplication
from ocr_engine import ocr_image
from translator import translate_text
from overlay import TranslationOverlay
import logging

class ScreenshotWindow(QWidget):
    def __init__(self):
        super().__init__()
        # Set as a frameless window that stays on top (a "tool" window)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        # Enable a transparent background
        self.setAttribute(Qt.WA_TranslucentBackground)
        # We don't want to delete the widget when it's "closed", just hide it
        self.setAttribute(Qt.WA_DeleteOnClose, False)
        
        self.begin = None
        self.end = None
        self.overlay = None

    def paintEvent(self, event):
        painter = QPainter(self)
        # Dim the entire screen with a semi-transparent black overlay
        painter.fillRect(self.rect(), QColor(0, 0, 0, 100))

        if self.begin and self.end:
            selection_rect = QRect(self.begin, self.end).normalized()
            # Clear the selected area so the screen underneath is visible
            painter.setCompositionMode(QPainter.CompositionMode_Clear)
            painter.fillRect(selection_rect, Qt.transparent)
            painter.setCompositionMode(QPainter.CompositionMode_SourceOver)
            # Draw a red border around the clear selection
            painter.setPen(QPen(QColor("red"), 2))
            painter.drawRect(selection_rect)

    def mousePressEvent(self, event):
        self.begin = event.pos()
        self.end = self.begin
        self.update()

    def mouseMoveEvent(self, event):
        self.end = event.pos()
        self.update()

    def mouseReleaseEvent(self, event):
        # Hide the selection window
        self.hide()
        # Use a short timer to ensure the window is fully hidden before taking the screenshot
        QTimer.singleShot(100, self.capture_screen)

    def capture_screen(self):
        if not self.begin or not self.end:
            return

        screen = QGuiApplication.primaryScreen()
        selection_rect = QRect(self.begin, self.end).normalized()
        
        x, y = selection_rect.x(), selection_rect.y()
        w, h = selection_rect.width(), selection_rect.height()

        # Grab the content of the desktop at the selected coordinates
        screenshot = screen.grabWindow(QApplication.desktop().winId(), x, y, w, h)
        screenshot_path = "screenshot.png"
        screenshot.save(screenshot_path, "png")
        logging.info(f"Screenshot saved to {screenshot_path}")

        extracted_text = ocr_image(screenshot_path)
        if extracted_text:
            translated_text = translate_text(extracted_text)
            self.show_translation(translated_text, x, y, w, h)

    def show_translation(self, text, x, y, width, height):
        # If an old overlay exists, close it before creating a new one
        if self.overlay and self.overlay.isVisible():
            self.overlay.close()
        self.overlay = TranslationOverlay(text, x, y, width, height)
        self.overlay.show()

    def start_selection(self):
        """Shows the window in fullscreen to allow the user to make a selection."""
        logging.info("Starting screen selection...")
        self.begin = None
        self.end = None
        self.showFullScreen()
        self.raise_()
        self.activateWindow()