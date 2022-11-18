from psycopg2 import Error
from connection import Conexao

def insertMultiLine(records):
    try:
        # conecta ao banco:
        connection = Conexao(user="sysadmin", password="pynative@#29", 
                                host="127.0.0.1", port="5432", database="postgres_db")

        # criar cursor para gerenciar o banco:
        cursor = connection.cursor()
        sql_insert_query = f""" INSERT INTO mobile (id, model, price) 
                           VALUES (%s,%s,%s) """

        # executemany() para inserir multiplas linhas:
        result = cursor.executemany(sql_insert_query, records)
        connection.commit()

        
        print(f"TOTAL DE LINHAS INSERIDAS: {cursor.rowcount}")
        print('#### SUCESSO ####')

    except (Exception, Error) as error:
        print("Failed inserting record into mobile table {}".format(error))

    finally:
        # Fechando a conexão.
        connection.close_cursor_conection()



# Exemplo:
records_to_insert = [(4, 'LG', 800), (5, 'One Plus 6', 950)]
insertMultiLine(records_to_insert)