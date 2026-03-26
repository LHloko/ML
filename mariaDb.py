# Criar um Crud Simples em Python 

# importando a biblioteca mysql-connector-python
import mysql.connector

# cria a conexao e testa 
def conectar(): 
    try: 
        conexao = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="lhroot1.",
        database="meu_banco"
        )
    
        if conexao.is_connected():
            return conexao
        
    except mysql.connector.Error as err: 
        print(f"Erro: {err}")
        return None

# CREATE - insert into usuarios
def cadastrar_usuario(name,dataNasc,endereco,email):
    try: 
        conexao = conectar()
        if conexao is None:
            return False

        cursor = conexao.cursor()

        sql = "INSERT INTO usuarios (nome, data_nascimento, endereco, email) VALUES (%s, %s, %s, %s)"
        values = (name, dataNasc, endereco, email)

        cursor.execute(sql,values)
        conexao.commit() 

        print(f"Usuario {name} registrado com sucesso !")
        return True
    
    except mysql.connector.Error as err: 
        print(f"Erro: {err}")
        return False 
    
    finally:    
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals() and conexao.is_connected():
            conexao.close()
# CREATE - insert into destinos
def cadastrar_destino(nome, descricao):
    try:
        conexao = conectar()

        if conexao is None:
            return False
        
        cursor = conexao.cursor()

        sql = "INSERT INTO destinos (nome, descricao) VALUES (%s,%s)"
        values = (nome, descricao)

        cursor.execute(sql,values)
        conexao.commit()

        print(f"Destino {nome} registrado com sucesso!")
        return True 

    except mysql.connector.Error as err:
        print(f"Erro: {err}")
        return False
    
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals() and conexao.is_connected():
            conexao.close()
# CREATE - inser into reservas
def cadastrar_reserva(dataReserva,id_usuario,id_destino):
    try: 
        conexao = conectar()
        if conexao is None: 
            return False
        
        cursor = conexao.cursor()

        sql = "INSERT INTO reservas (data_reserva, id_usuario, id_destino) VALUES (%s,%s,%s)"
        values=(dataReserva, id_usuario, id_destino)

        cursor.execute(sql,values)
        conexao.commit()

        print(f"O User [nome] fez uma reserva para [destino] na data de {dataReserva}")
        return True 

    except mysql.connector.Error as err:
        print(f"Erro: {err}")
        return False 
    
    finally: 
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals() and conexao.is_connected():
            conexao.close()

# SELECT - lista de reservas do usuario 
def select_user(user_id):
    try:
        cnx = conectar();
        
        if cnx is None:
            return False
        
        cursor = cnx.cursor(dictionary=True)
        sql =   """
                SELECT 
                    usuarios.nome AS usuario,
                    reservas.data_reserva,
                    destinos.nome as destino
                FROM reservas
                INNER JOIN usuarios
                    ON usuarios.id = reservas.id_usuario
                INNER JOIN destinos 
                    ON destinos.id = reservas.id_destino
                WHERE usuarios.id = (%s)
                """
        values = (user_id,)
        cursor.execute(sql,values)
        resultado = cursor.fetchall()
        
        print(resultado)
        return True

    except mysql.connector.Error as err: 
        print(f"Erro:{err}")
        return False
    
    finally:    
        if 'cursor' in locals():
            cursor.close()
        if 'cnx' in locals() and cnx.is_connected():
            cnx.close()
# SELECT - lista de reservas do destino
def select_destino(destino_id):
    try: 
        cnx = conectar()
        if cnx is None:
            return False 
        
        crs = cnx.cursor(dictionary=True)
        sql =   """
                SELECT 
                    usuarios.nome AS usuario,
                    reservas.data_reserva as data,
                    destinos.nome AS destino
                FROM reservas
                INNER JOIN destinos
                    ON destinos.id = reservas.id_destino
                INNER JOIN usuarios 
                    ON usuarios.id = reservas.id_usuario
                WHERE destinos.id = (%s)
                """
        values = (destino_id,)
        crs.execute(sql,values)
        print(crs.fetchall())
        return True 

    except mysql.connector.Error as err:
        print(f"Erro: {err}")
        return False

    finally:
        if 'crs' in locals():
            crs.close()
        if 'cnx' in locals() and cnx.is_connected():
            cnx.close()
# SELECT - lista de reservas
def select_reserva(reserva_id):
    try: 
        cnx = conectar()
        if cnx is None:
            return False 
        
        crs = cnx.cursor(dictionary=True)
        sql =   """
                SELECT 
                    usuarios.nome AS usuario,
                    reservas.data_reserva as data,
                    destinos.nome AS destino
                FROM reservas
                INNER JOIN destinos
                    ON destinos.id = reservas.id_destino
                INNER JOIN usuarios 
                    ON usuarios.id = reservas.id_usuario
                WHERE reservas.id = (%s)
                """
        values = (reserva_id,)
        crs.execute(sql,values)
        print(crs.fetchall())
        return True 

    except mysql.connector.Error as err:
        print(f"Erro: {err}")
        return False

    finally:
        if 'crs' in locals():
            crs.close()
        if 'cnx' in locals() and cnx.is_connected():
            cnx.close()

# DELETE - deleta uma reserva
def delete_reserva(reserva_id):
    try: 
        cnx = conectar()
        if cnx is None:
            return False
        
        crs = cnx.cursor()
        sql =   """
                DELETE FROM reservas 
                WHERE id = (%s)
                """
        values = (reserva_id,)
        crs.execute(sql,values)

        print("A Reserva foi deletada: ", end=" ")
        select_reserva(reserva_id)
        
        cnx.commit()
        return True

    except mysql.connector.Error as err:
        print(f"Erro: {err}")
        return False
    
    finally: 
        if 'crs' in locals():
            crs.close()
        if 'cnx' in locals() and cnx.is_connected():
            cnx.close()

def main(): 
    print("sim")

main()