import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QMainWindow, QLabel
from variaveis import WINDOW_ICON_PATH

from main_window import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    #Define o icone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    label1 = QLabel('O meu label')
    label1.setStyleSheet('font-size: 30px')
    window.addWidgetToLayout(label1)
    
    window.ajustFixedSize()
    window.show()
    app.exec()

# --- EXECUÇÃO DO APLICATIVO ---
# if __name__ == '__main__':
#     app = QApplication(sys.argv)                 # Inicializa o motor do Qt
#     window = MainWindow()                        # Cria a janela calculadora

#     label1 = QLabel('O meu label')               # Cria um texto
#     label1.setStyleSheet('font-size: 30px')      # Aumenta a fonte do texto para 30px
#     window.v_layout.addWidget(label1)            # Coloca o texto dentro do layout da janela
#     window.ajustFixedSize()                      # Ajusta e trava o tamanho da janela

#     window.show()                                # Exibe a janela na tela
#     app.exec()                                   # Roda o aplicativo até ser fechado