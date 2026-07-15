import sys
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QMainWindow, QLabel

class MainWindow(QMainWindow):
    def __init__(self, /, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        self.cw = QWidget()
        self.v_layout = QVBoxLayout()
        self.cw.setLayout(self.v_layout)
        self.setCentralWidget(self.cw)
        
        self.setWindowTitle('Calculadora')


    def ajustFixedSize(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())
    