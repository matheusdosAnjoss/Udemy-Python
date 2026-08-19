from PySide6.QtWidgets import QLineEdit
from variaveis import BIG_FONT_SIZE, TEXT_MARGIN
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QKeyEvent
from utils import isEmpty, isNumOrDot

# Display é um QLineEdit personalizado que funciona como o visor da calculadora.
# Ele configura tamanho, fonte, alinhamento e margens do campo.
# Também detecta quando o usuário pressiona Enter e emite o sinal
# "eqRequested" para avisar que a expressão deve ser calculada.

class Display(QLineEdit):
    eqPressed = Signal()
    delPressed = Signal()
    clearPressed = Signal()
    inputPressed = Signal(str)
    operatorPressed = Signal(str)


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
        text = event.text().strip()
        key = event.key()
        KEYS = Qt.Key

        isEnter = key in [KEYS.Key_Enter, KEYS.Key_Return]
        isDelete = key in [KEYS.Key_Backspace, KEYS.Key_Delete]
        isEsc = key in [KEYS.Key_Escape, KEYS.Key_C]
        isOperator = key in [
            KEYS.Key_Plus, KEYS.Key_Minus, KEYS.Key_Slash, KEYS.Key_Asterisk, KEYS.Key_P,
            ]
        
        if isEnter or text == '=':
            self.eqPressed.emit()
            return event.ignore()

        if isDelete or text.lower() == 'd':
            self.delPressed.emit()
            return event.ignore()

        if isEsc or text.lower() == 'c':
            self.clearPressed.emit()
            return event.ignore()

        if isOperator:
            if text.lower() == 'p':
                text = '^'
            self.operatorPressed.emit(text)
            return event.ignore()

        # Não passar daqui se não tiver texto
        if isEmpty(text):
            return event.ignore()

        print('Texto', text)

        if isNumOrDot(text):
            self.inputPressed.emit(text)
            return event.ignore()