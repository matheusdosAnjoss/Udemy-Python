from PySide6.QtWidgets import QLineEdit
from variaveis import BIG_FONT_SIZE, TEXT_MARGIN
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QKeyEvent

class Display(QLineEdit):
    eqRequested = Signal()   


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        margins = [TEXT_MARGIN for _ in range(4)]
        self.setStyleSheet(f"font-size: {BIG_FONT_SIZE}px")
        self.setMinimumHeight(BIG_FONT_SIZE * 2)
        self.setMinimumWidth(500)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*margins)

    def keyPressEvent(self, event: QKeyEvent) -> None:
        key = event.key()
        KEYS = Qt.Key

        isEnter = key in [KEYS.Key_Enter, KEYS.Key_Return]

        if isEnter:
            print('precionou enter')
            self.eqRequested.emit()
            return event.ignore()