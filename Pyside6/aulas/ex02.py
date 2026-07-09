import sys
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QMainWindow

app = QApplication(sys.argv) # 1. Cria o aplicativo
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)

botao = QPushButton('Texto botao')# 2. Cria o botão
botao.setStyleSheet('font-size: 50px; color: white') # 3. Estiliza (tamanho e cor)

botao2 = QPushButton('botao 2')# 2. Cria o botão
botao2.setStyleSheet('font-size: 50px; color: white') 

# botao.show() # 4. Mostra o botão na tela

layout = QVBoxLayout()
central_widget.setLayout(layout)

layout.addWidget(botao)
layout.addWidget(botao2)


window.show()
app.exec()# 5. Mantém a janela aberta



# # -------------------------------------------------
# # Cria a aplicação Qt
# # Todo programa PySide precisa de um QApplication
# # -------------------------------------------------
# app = QApplication(sys.argv)

# # -------------------------------------------------
# # Cria a janela principal do programa
# # -------------------------------------------------
# window = QMainWindow()

# # -------------------------------------------------
# # Cria um widget central.
# # O QMainWindow precisa de um widget central para
# # armazenar outros componentes (botões, textos, etc.)
# # -------------------------------------------------
# central_widget = QWidget()

# # Define o widget criado como o widget central da janela
# window.setCentralWidget(central_widget)

# # -------------------------------------------------
# # Cria o primeiro botão
# # -------------------------------------------------
# botao = QPushButton('Texto botao')

# # Define o estilo do botão utilizando CSS
# # font-size -> tamanho da fonte
# # color -> cor do texto
# botao.setStyleSheet('font-size: 50px; color: white')

# # -------------------------------------------------
# # Cria o segundo botão
# # -------------------------------------------------
# botao2 = QPushButton('botao 2')

# # Aplica o mesmo estilo ao segundo botão
# botao2.setStyleSheet('font-size: 50px; color: white')

# # -------------------------------------------------
# # Caso o botão fosse mostrado sozinho:
# # botao.show()
# #
# # Como estamos utilizando uma janela principal,
# # os botões serão adicionados ao layout e não
# # precisam do método show() individualmente.
# # -------------------------------------------------

# # Cria um layout vertical
# # Os widgets adicionados ficarão um abaixo do outro
# layout = QVBoxLayout()

# # Define esse layout para o widget central
# central_widget.setLayout(layout)

# # Adiciona o primeiro botão ao layout
# layout.addWidget(botao)

# # Adiciona o segundo botão abaixo do primeiro
# layout.addWidget(botao2)

# # -------------------------------------------------
# # Exibe a janela principal
# # -------------------------------------------------
# window.show()

# # -------------------------------------------------
# # Inicia o loop de eventos da aplicação.
# # O programa permanecerá aberto até que
# # a janela seja fechada.
# # -------------------------------------------------
# app.exec()