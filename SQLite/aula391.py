import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# CUIDADO: FAZENDO DELETE SEM WHERE
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)
connection.commit()

# CRIA A TABELA
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} '
    '(id INTEGER PRIMARY KEY AUTOINCREMENT, '
    'name TEXT, '
    'weight REAL)'
)
connection.commit()

# REGISTRA VALOR NAS COLUNAS
cursor.execute(
    f'INSERT INTO {TABLE_NAME} (id, name, weight) '
    'VALUES ' 
    "(NULL, 'Luis Otavio', 9.9), (NULL, 'Matheus', 7.5)"
)
connection.commit()


cursor.close()
connection.close()