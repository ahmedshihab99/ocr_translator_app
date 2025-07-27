from PyQt5.QtWidgets import QWidget, QLabel, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class TranslationOverlay(QWidget):
    def __init__(self, text, x, y, width, height):
        super().__init__()
        self.setGeometry(x, y, width, height)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.label = QLabel(text, self)
        self.label.setGeometry(10, 10, width - 20, height - 20)
        self.label.setWordWrap(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("background-color: rgba(0, 0, 0, 180); color: white; border-radius: 5px;")
        self.label.setFont(QFont("Arial", 12))

        self.close_button = QPushButton("X", self)
        self.close_button.setGeometry(width - 30, 0, 30, 30)
        self.close_button.setStyleSheet("background-color: red; color: white; border-radius: 15px; font-weight: bold;")
        self.close_button.clicked.connect(self.close)