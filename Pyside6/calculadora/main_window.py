import sys
from PySide6.QtGui import QIcon
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

    def addWidgetToLayout(self, widget: QWidget):
        self.v_layout.addWidget(widget)
        
    

    # --- DEFINIÇÃO DA JANELA PRINCIPAL ---
# class MainWindow(QMainWindow):
#     def __init__(self, /, parent: QWidget | None = None, *args, **kwargs) -> None:
#         super().__init__(parent, *args, **kwargs) # Inicializa a classe base (QMainWindow)

        # self.cw = QWidget()                      # Cria o widget central (container)
        # self.v_layout = QVBoxLayout()            # Cria o layout vertical (alinha itens em pé)
        # self.cw.setLayout(self.v_layout)         # Associa o layout ao container
        # self.setCentralWidget(self.cw)           # Define o container como o centro da janela
        
        # self.setWindowTitle('Calculadora')        # Define o título da janela

    # def ajustFixedSize(self):
    #     self.adjustSize()                        # Ajusta a janela ao tamanho do conteúdo
    #     self.setFixedSize(self.width(), self.height()) # Trava a janela nesse tamanho (impede redimensionar)