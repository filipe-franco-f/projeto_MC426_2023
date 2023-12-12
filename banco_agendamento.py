import sqlite3
import json
from agendamento_reunioes.agendamento_exceptions import CampoVazioException, DataInvalidaException, PessoaNaoEncontrada, reuniaoNaoEncontrada
import comunidade
import Bancologin

# Conecta-se ao banco de dados (ou cria um novo se não existir)
conn = sqlite3.connect('dadologin.db')

# Cria um cursor para executar comandos SQL
cursor = conn.cursor()

# Cria uma tabela para armazenar os dados
cursor.execute('''CREATE TABLE IF NOT EXISTS agendamento (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL UNIQUE,
                    reunioes TEXT DEFAULT "[]"
                )''')

# Salva as alterações no banco de dados
conn.commit()

# Fecha a conexão com o banco de dados
conn.close()
def inserir_no_banco(id, username):
    try:
        conn = sqlite3.connect('dadologin.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO agendamento (id, username, reunioes) VALUES(?, ?, ?)", [id, username, "[]"])
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
        cursor.execute("DELETE FROM agendamento WHERE username=?", (username,))
        conn.commit()
        conn.close()
        return "usuario deletado com sucesso"
    except:
        return "erro ao tentar apagar usuario"
    
def get_username(id):
    conn = sqlite3.connect('dadologin.db')
    cursor = conn.cursor()
    cursor.execute("SELECT username FROM agendamento WHERE id=?", (id,))
    resultado = cursor.fetchone()
    conn.close()
    if resultado:
        return resultado[0]
    else:
        return None

def get_id(username):
    conn = sqlite3.connect('dadologin.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM agendamento WHERE username=?", (username,))
    resultado = cursor.fetchone()
    conn.close()
    if resultado:
        return resultado[0]
    else:
        return None
    
def cadastra_reuniao_uma_pessoa(username1:str, data_hora:str, assunto:str):
    conn = sqlite3.connect('dadologin.db')
    cursor = conn.cursor()
    cursor.execute("SELECT reunioes FROM agendamento WHERE username=?", (username1,))
    resultado = cursor.fetchone()[0]
    conn.close()
    res = json.loads(resultado)
    res.append([data_hora, assunto])
    res = json.dumps(res)
    conn = sqlite3.connect('dadologin.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE agendamento SET reunioes =? WHERE username=?", (res, username1))
    conn.commit()
    conn.close()

    
def cadastra_reuniao(id_user:int, data_hora:str, assunto:str):
    username1 = get_username(id_user)
    cadastra_reuniao_uma_pessoa(username1, data_hora, assunto)
    notificacao1 = f"Voce cadastrou uma reunião para sua comunidade sobre {assunto}, em: {data_hora}."
    Bancologin.alt_dado(6, id_user, notificacao1,"add")
    
    lista_de_comunidade = comunidade.lista_amigos(id_user)
    for pessoa in lista_de_comunidade:
        if pessoa != username1:
            cadastra_reuniao_uma_pessoa(pessoa, data_hora, assunto)
            id_pessoa = get_id(pessoa)
            notificacao2 = f"{username1} cadastrou uma reunião para sua comunidade sobre {assunto}, em: {data_hora}."
            Bancologin.alt_dado(6, id_pessoa, notificacao2,"add")
    
    
def checar_reunioes(id:int):
    conn = sqlite3.connect('dadologin.db')
    cursor = conn.cursor()
    cursor.execute("SELECT reunioes FROM agendamento WHERE id=?", (id,))
    resultado = cursor.fetchone()
    conn.close()
    if resultado:
        return json.loads(resultado[0])
    else:
        return None
    
def deleta_reuniao_uma_pessoa(username1:str, data_hora:str, assunto:str):
    conn = sqlite3.connect('dadologin.db')
    cursor = conn.cursor()
    cursor.execute("SELECT reunioes FROM agendamento WHERE username=?", (username1,))
    resultado = cursor.fetchone()[0]
    conn.close()
    res = json.loads(resultado)
    try:
        res.remove([data_hora, assunto])
    except:
        raise reuniaoNaoEncontrada
    res = json.dumps(res)
    conn = sqlite3.connect('dadologin.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE agendamento SET reunioes =? WHERE username=?", (res, username1))
    conn.commit()
    conn.close()

def deletar_reuniao(id_user:int, data_hora:str, assunto:str):
    username1 = get_username(id_user)
    if username1 == None:
        raise PessoaNaoEncontrada
    try:
        deleta_reuniao_uma_pessoa(username1, data_hora, assunto)
        notificacao1 = f"Voce desmarcou uma reunião para sua comunidade sobre {assunto}, em: {data_hora}."
        Bancologin.alt_dado(6, id_user, notificacao1,"add")
    except:
        raise reuniaoNaoEncontrada
    lista_de_comunidade = comunidade.lista_amigos(id_user)
    for pessoa in lista_de_comunidade:
        if pessoa != username1:
            deleta_reuniao_uma_pessoa(pessoa, data_hora, assunto)
            id_pessoa = get_id(pessoa)
            notificacao2 = f"{username1} desmarcou uma reunião para sua comunidade sobre {assunto}, em: {data_hora}."
            Bancologin.alt_dado(6, id_pessoa, notificacao2,"add")
    