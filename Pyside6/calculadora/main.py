import sys
from buttons import ButtonsGrid
from display import Display
from info import Info
from main_window import MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from style import setupTheme
from variaveis import WINDOW_ICON_PATH

if __name__ == '__main__':
    # Cria a aplicação
    app = QApplication(sys.argv)
    setupTheme(app)
    window = MainWindow()
 
    # Define o ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)
 
    # Info
    info = Info('')
    window.addWidgetToVLayout(info)
 
    # Display
    display = Display()
    window.addWidgetToVLayout(display)
 
    #Grid
    buttonsGrid = ButtonsGrid(display, info, window)
    window.vLayout.addLayout(buttonsGrid)

    # Executa tudo
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