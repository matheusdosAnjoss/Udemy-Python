import pymysql
import pymysql.cursors
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
    cursorclass=pymysql.cursors.DictCursor,
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

    # Inserindo um cliente com tupla
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
        # print(sql)
        # print(result)
    connection.commit()

    # Inserindo usando um dicionário
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
        # print(sql)
        # print(data2)
        # print(result)
    connection.commit()

    # Inserindo vários clientes com executemany()
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%(nome)s, %(idade)s) '
        )
        
        data3 = (
            {"nome": "Diego", "idade": 43,},
            {"nome": "Ana", "idade": 23,},
            {"nome": "Ze", "idade": 49,},
        )

        result = cursor.executemany(sql, data3)
        # print(sql)
        # print(data3)
        # print(result)
    connection.commit()

    #4. Outra forma de usar executemany()
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%s, %s) '
        )
        
        data4 = (
            ("Sara", 12 ),
            ("Elena", 13 ),
        )

        result = cursor.executemany(sql, data4)
        # print(sql)
        # print(data4)
        # print(result)
    connection.commit()


    # Lendo os valores com SELECT
    with connection.cursor() as cursor:
        # menor_id = int(input('Digite o menor id: '))
        # maior_id = int(input('Digite o maior id: '))
        menor_id = 2
        maior_id = 4

        sql = (
            f'SELECT * FROM {TABLE_NAME} '
            f'WHERE id BETWEEN %s AND %s '
        )

        cursor.execute(sql, (menor_id, maior_id))  
        # print(cursor.mogrify(sql, (menor_id, maior_id)))
        data5 = cursor.fetchall()  # type: ignore

        # for row in data5:
        #     print(row)

    # Apagando valores com DELETE
    with connection.cursor() as cursor:
        sql = (
            f'DELETE FROM {TABLE_NAME} '
            f'WHERE id = %s'
        )

        cursor.execute(sql, (1))
        connection.commit()
        
        cursor.execute(f'SELECT * FROM {TABLE_NAME} ')  
        
        # for row in cursor.fetchall():
        #     print(row)
   

   # Editando com UPDATE
    with connection.cursor() as cursor:
        sql = (
            f'UPDATE {TABLE_NAME} '
            'SET nome=%s, idade=%s '
            'WHERE id=%s'
        )
    
        cursor.execute(sql, ('Gustavo', 35, 5))
        cursor.execute(f'SELECT * FROM {TABLE_NAME} ')  
            
        for row in cursor.fetchall():
            print(row)
    connection.commit()




