import sqlite3
import json
import Bancologin

class PessoaNaoEncontrada(LookupError):
    pass

class DividaNaoEncontrada(LookupError):
    pass

class DbParams:
    def __init__(self, id, username, valor, assunto):
        self.id = id
        self.username = username
        self.valor = valor
        self.assunto = assunto


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
    
def cadastra_divida_uma_pessoa(db_params_user1: DbParams, db_params_user2: DbParams):
    conn = sqlite3.connect('dadologin.db')
    cursor = conn.cursor()
    cursor.execute("SELECT dividas FROM financas WHERE username=?", (db_params_user1.username,))
    resultado = cursor.fetchone()[0]
    conn.close()
    res = json.loads(resultado)
    res.append([db_params_user2.username, db_params_user1.valor, db_params_user1.assunto])
    res = json.dumps(res)
    conn = sqlite3.connect('dadologin.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE financas SET dividas =? WHERE username=?", (res, db_params_user1.username))
    conn.commit()
    conn.close()

    
def cadastra_divida(db_params_user1: DbParams, db_params_user2: DbParams):
    db_params_user2.valor = str(float(db_params_user1.valor) *-1)
    db_params_user2.assunto = db_params_user1.assunto
    db_params_user1.username = get_username(db_params_user1.id)
    db_params_user2.id = get_id(db_params_user2.username)
    if db_params_user1.username == None or db_params_user2.id == None:
        raise PessoaNaoEncontrada
    cadastra_divida_uma_pessoa(db_params_user1, db_params_user2)
    cadastra_divida_uma_pessoa(db_params_user2, db_params_user1)
    notificacao1 = f"Voce cadastrou dívida para {db_params_user2.username} de {db_params_user1.valor} sobre {db_params_user1.assunto}."
    notificacao2 = f"{db_params_user1.username} cadastrou divida para você no valor de {db_params_user2.valor} sobre {db_params_user2.assunto}."
    Bancologin.alt_dado(6, db_params_user1.id, notificacao1,"add")
    Bancologin.alt_dado(6, db_params_user2.id, notificacao2,"add")

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
    
def quita_divida_uma_pessoa(db_params_user1: DbParams, db_params_user2: DbParams):
    conn = sqlite3.connect('dadologin.db')
    cursor = conn.cursor()
    cursor.execute("SELECT dividas FROM financas WHERE username=?", (db_params_user1.username,))
    resultado = cursor.fetchone()[0]
    conn.close()
    res = json.loads(resultado)
    try:
        res.remove([db_params_user2.username, db_params_user1.valor, db_params_user1.assunto])
    except:
        raise DividaNaoEncontrada
    res = json.dumps(res)
    conn = sqlite3.connect('dadologin.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE financas SET dividas =? WHERE username=?", (res, db_params_user1.username))
    conn.commit()
    conn.close()

def quitar_divida(db_params_user1: DbParams, db_params_user2:DbParams):
    db_params_user2.valor = str(float(db_params_user1.valor) *-1)
    db_params_user2.assunto = db_params_user1.assunto
    db_params_user1.username = get_username(db_params_user1.id)
    db_params_user2.id = get_id(db_params_user2.username)
    if db_params_user1.username == None or db_params_user2.id == None:
        raise PessoaNaoEncontrada
    try:
        quita_divida_uma_pessoa(db_params_user1, db_params_user2)
        quita_divida_uma_pessoa(db_params_user2, db_params_user1)
    except:
        raise DividaNaoEncontrada
    notificacao1 = f"Voce quitou dívida para {db_params_user2.username} de {db_params_user1.valor} sobre {db_params_user1.assunto}."
    notificacao2 = f"{db_params_user1.username} quitou divida para você no valor de {db_params_user2.valor} sobre {db_params_user2.assunto}."
    Bancologin.alt_dado(6, db_params_user1.id, notificacao1,"add")
    Bancologin.alt_dado(6, db_params_user2.id, notificacao2,"add")
    
