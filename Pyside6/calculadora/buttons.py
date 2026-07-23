from PySide6.QtWidgets import QPushButton, QWidget, QGridLayout
from utils import isEmpty, isNumOrDot

class Button(QPushButton):
    def __init__(self, /, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        self.consfigStyle()

    def consfigStyle(self):
        self.setStyleSheet(f'font-size: 24px')
        self.setMinimumSize(75, 75)


class ButtonsGrid(QGridLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._gridMask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
        ]

        self._makeGrid()

    def _makeGrid(self):
        for i, rowData in enumerate(self._gridMask):
            for j, button_text in enumerate(rowData):
                button = Button(button_text)

                if not isNumOrDot(button_text) and not isEmpty(button_text):
                    button.setProperty('cssClass', 'specialButton')
                
                self.addWidget(button, i, j)