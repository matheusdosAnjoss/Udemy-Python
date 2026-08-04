from PySide6.QtWidgets import QPushButton, QWidget, QGridLayout
from PySide6.QtCore import Slot
from utils import isEmpty, isNumOrDot, isValidNumber
from display import Display
import math

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from display import Display
    from info import Info


class Button(QPushButton):
    def __init__(self, /, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        self.consfigStyle()

    def consfigStyle(self):
        self.setStyleSheet(f'font-size: 24px')
        self.setMinimumSize(75, 75)


class ButtonsGrid(QGridLayout):
    def __init__(self, display: 'Display', info: 'Info', *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._gridMask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
        ]
        self.info = info
        self.display = display
        self._equation = ''
        self._equationInitalValue = 'Sua conta'
        self._left = None
        self._right = None  
        self._op = None

        self.equation = self._equationInitalValue
        self._makeGrid()

    @property
    def equation(self):
        return self._equation

    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)

    def _makeGrid(self):
        for i, rowData in enumerate(self._gridMask):
            for j, button_text in enumerate(rowData):
                button = Button(button_text)

                if not isNumOrDot(button_text) and not isEmpty(button_text):
                    button.setProperty('cssClass', 'specialButton')
                    self._configSpecialButton(button)
                
                self.addWidget(button, i, j)

                slot = self._makeSlot(self._inserButtonTextToDisplay, button)
                self._conectButtonClicked(button, slot)

    def _conectButtonClicked(self, button, slot):
        button.clicked.connect(slot)

    def _configSpecialButton(self, button):
        text = button.text()

        if text == 'C':
            self._conectButtonClicked(button, self._clear)

        if text in '+-*/^':
            self._conectButtonClicked(
                button,
                self._makeSlot(self._operatorClicked, button)
            )


        if text in '=':
            self._conectButtonClicked(button, self._eq)
            
            
    def _makeSlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot(_):
            func(*args, **kwargs)
        return realSlot
        

    def _inserButtonTextToDisplay(self, button):
        button_text = button.text()
        newDisplayValue = self.display.text() + button_text

        if not isValidNumber(newDisplayValue):
            return

        self.display.insert(button_text)

    def _clear(self):
        self._left = None
        self._right = None  
        self._op = None
        self.equation = self._equationInitalValue
        self.display.clear()

    def _operatorClicked(self, button):
        buttonText = button.text()
        displayText = self.display.text()
        self.display.clear()

        if not isValidNumber(displayText) and self._left is None:
            print('nao tem nada para colocar no valor da esquerda')
            return

        if self._left is None:
            self._left = float(displayText)

        self._op = buttonText
        self.equation = f'{self._left} {self._op} ??'

    def _eq(self):
        
        displayText = self.display.text()

        if not isValidNumber(displayText):
            print('sem nada para a direita')
            return

        self._right = float(displayText)
        self.equation = f'{self._left} {self._op} {self._right}'
        result = 'error'

        try:
            if '^' in self.equation and isinstance(self._left, float):
                result = math.pow(self._left, self._right)
            else:
                result = eval(self.equation)
        except ZeroDivisionError:
           print("zero division ERROR")
        except OverflowError:
            print('número muito grande')

        self.display.clear()
        self.info.setText(f'{self.equation} = {result}')
        self._left = result
        self._right = None

        if result == 'error':
            self._left = None



        