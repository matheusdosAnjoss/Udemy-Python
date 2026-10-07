import pymysql
import os
import dotenv

dotenv.load_dotenv()
TABLE_NAME = 'customers'

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    port=3307,
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    charset='utf8mb4',
)

print(os.environ['MYSQL_DATABASE'])


with connection:
    with connection.cursor() as cursor:
        # 1. CREATE TABLE
        cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                id INT NOT NULL AUTO_INCREMENT,
                nome VARCHAR(50) NOT NULL,
                idade INT NOT NULL,
                PRIMARY KEY (id)
            )
        ''')
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')
    connection.commit()

    with connection.cursor() as cursor:
        #SQL
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%s, %s) '
        )
        data = ('Luiz', 18)
        result = cursor.execute(sql, data) # type: ignore
        print(sql)
        print(result)
    connection.commit()

    with connection.cursor() as cursor:
        #SQL
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%(nome)s, %(idade)s) '
        )
        data2 = {
            "nome": "João",
            "idade": 37,
        }
        result = cursor.execute(sql, data2)
        print(sql)
        print(data2)
        print(result)
    connection.commit()







