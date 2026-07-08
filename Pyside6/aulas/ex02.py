import sys
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout

app = QApplication(sys.argv) # 1. Cria o aplicativo

botao = QPushButton('Texto botao')# 2. Cria o botão
botao.setStyleSheet('font-size: 50px; color: white') # 3. Estiliza (tamanho e cor)
# botao.show() # 4. Mostra o botão na tela

central_widget = QWidget()

layout = QVBoxLayout()
central_widget.setLayout(layout)

layout.addWidget(botao)


central_widget.show()
app.exec()# 5. Mantém a janela aberta