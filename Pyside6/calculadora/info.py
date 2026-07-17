from PySide6.QtWidgets import QLabel, QWidget
from PySide6.QtCore import Qt

class Info(QLabel):
    def __init__(self, /, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        self.consfigStyle()

    def consfigStyle(self):
        self.setStyleSheet(f'font-size: 18px')
        self.setAlignment(Qt.AlignmentFlag.AlignRight)