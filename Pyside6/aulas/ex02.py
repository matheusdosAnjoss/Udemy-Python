import sys
from PySide6.QtWidgets import QApplication, QPushButton

app = QApplication(sys.argv) # 1. Cria o aplicativo

botao = QPushButton('Texto botao')# 2. Cria o botão
botao.setStyleSheet('font-size: 50px; color: white') # 3. Estiliza (tamanho e cor)
botao.show() # 4. Mostra o botão na tela

app.exec()# 5. Mantém a janela aberta