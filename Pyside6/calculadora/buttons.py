from PySide6.QtWidgets import QPushButton, QWidget

class Button(QPushButton):
    def __init__(self, /, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        self.consfigStyle()

    def consfigStyle(self):
        self.setStyleSheet(f'font-size: 24px')
        self.setMinimumSize(75, 75)
        self.setProperty('cssClass', 'specialButton')