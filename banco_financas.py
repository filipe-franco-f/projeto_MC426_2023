import sqlite3
import json
import traceback
import sys

class PessoaNaoEncontrada(LookupError):
    pass

class DividaNaoEncontrada(LookupError):
    pass


# Conecta-se ao banco de dados (ou cria um novo se não existir)
conn = sqlite3.connect('dadologin.db')

# Cria um cursor para executar comandos SQL
cursor = conn.cursor()

# Cria uma tabela para armazenar os dados
cursor.execute('''CREATE TABLE IF NOT EXISTS financas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL UNIQUE,
                    dividas TEXT DEFAULT "[]"
                )''')

# Salva as alterações no banco de dados
conn.commit()

# Fecha a conexão com o banco de dados
conn.close()
def inserir_no_banco(id, username):
    try:
        conn = sqlite3.connect('dadologin.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO financas (id, username, dividas) VALUES(?, ?, ?)", [id, username, "[]"])
        conn.commit()  
        conn.close()
        text = "username salvo com sucesso"
        return text
    except:
        text = "erro de username"
        return text

def consulta(num):
    conn = sqlite3.connect('dadologin.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM financas WHERE id=?", (num,))
    resultado = cursor.fetchone()
    conn.close()
    if resultado:
        return resultado
    else:
        return "404"
    
def consulta_username(username):
    conn = sqlite3.connect('dadologin.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM financas WHERE username=?", (username,))
    resultado = cursor.fetchone()
    conn.close()
    if resultado:
        return resultado
    else:
        return "404"

def deletarusuario(username):
    try:
        conn = sqlite3.connect('dadologin.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM financas WHERE username=?", (username,))
        conn.commit()
        conn.close()
        return "usuario deletado com sucesso"
    except:
        return "erro ao tentar apagar usuario"
    
def get_username(id):
    conn = sqlite3.connect('dadologin.db')
    cursor = conn.cursor()
    cursor.execute("SELECT username FROM financas WHERE id=?", (id,))
    resultado = cursor.fetchone()
    conn.close()
    if resultado:
        return resultado[0]
    else:
        return None

def get_id(username):
    conn = sqlite3.connect('dadologin.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM financas WHERE username=?", (username,))
    resultado = cursor.fetchone()
    conn.close()
    if resultado:
        return resultado[0]
    else:
        return None
    
def cadastra_divida_uma_pessoa(username1:str, username2:str, valor:str, assunto:str):
    conn = sqlite3.connect('dadologin.db')
    cursor = conn.cursor()
    cursor.execute("SELECT dividas FROM financas WHERE username=?", (username1,))
    resultado = cursor.fetchone()[0]
    conn.close()
    res = json.loads(resultado)
    res.append([username2, valor, assunto])
    res = json.dumps(res)
    conn = sqlite3.connect('dadologin.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE financas SET dividas =? WHERE username=?", (res, username1))
    conn.commit()
    conn.close()

    
def cadastra_divida(id:int, username_outra_pessoa:str, valor:str, assunto:str):
    valor_op = str(float(valor) *-1)
    username1 = get_username(id)
    id2 = get_id(username_outra_pessoa)
    if username1 == None or id2 == None:
        raise PessoaNaoEncontrada
    cadastra_divida_uma_pessoa(username1, username_outra_pessoa, valor, assunto)
    cadastra_divida_uma_pessoa(username_outra_pessoa, username1, valor_op, assunto)

def checar_dividas(id:int):
    conn = sqlite3.connect('dadologin.db')
    cursor = conn.cursor()
    cursor.execute("SELECT dividas FROM financas WHERE id=?", (id,))
    resultado = cursor.fetchone()
    conn.close()
    if resultado:
        return json.loads(resultado[0])
    else:
        return None
    
def quita_divida_uma_pessoa(username1:str, username2:str, valor:str, assunto:str):
    conn = sqlite3.connect('dadologin.db')
    cursor = conn.cursor()
    cursor.execute("SELECT dividas FROM financas WHERE username=?", (username1,))
    resultado = cursor.fetchone()[0]
    conn.close()
    res = json.loads(resultado)
    try:
        res.remove([username2, valor, assunto])
    except:
        raise DividaNaoEncontrada
    res = json.dumps(res)
    conn = sqlite3.connect('dadologin.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE financas SET dividas =? WHERE username=?", (res, username1))
    conn.commit()
    conn.close()

def quitar_divida(id:int, username_outra_pessoa:str, valor:str, assunto:str):
    valor_op = str(float(valor) *-1)
    username1 = get_username(id)
    id2 = get_id(username_outra_pessoa)
    if username1 == None or id2 == None:
        raise PessoaNaoEncontrada
    try:
        quita_divida_uma_pessoa(username1, username_outra_pessoa, valor, assunto)
        quita_divida_uma_pessoa(username_outra_pessoa, username1, valor_op, assunto)
    except:
        raise DividaNaoEncontrada
    
