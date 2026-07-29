try:
    import qdarkstyle
except ModuleNotFoundError:
    qdarkstyle = None

from variaveis import (DARKER_PRIMARY_COLOR, DARKEST_PRIMARY_COLOR, PRIMARY_COLOR)
 
qss = f"""
    QPushButton[cssClass="specialButton"] {{
        color: #fff;
        background: {PRIMARY_COLOR};
        border-radius: 5px;
    }}
    QPushButton[cssClass="specialButton"]:hover {{
        color: #fff;
        background: {DARKER_PRIMARY_COLOR};
    }}
    QPushButton[cssClass="specialButton"]:pressed {{
        color: #fff;
        background: {DARKEST_PRIMARY_COLOR};
    }}
"""
 
 
def setupTheme(app):
    if qdarkstyle is not None:
        # Aplicar o estilo escuro do qdarkstyle
        app.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())

        # Sobrepor com o QSS personalizado para estilização adicional
        app.setStyleSheet(app.styleSheet() + qss)
    else:
        app.setStyleSheet(qss)