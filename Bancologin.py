import sqlite3

# Conecta-se ao banco de dados (ou cria um novo se não existir)
conn = sqlite3.connect('dadologin.db')

# Cria um cursor para executar comandos SQL
cursor = conn.cursor()

# Cria uma tabela para armazenar os dados
cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    login TEXT NOT NULL UNIQUE,
                    senha TEXT NOT NULL,
                    acumulador INTEGER DEFAULT 0,
                    bloqueado INTEGER DEFAULT 0,
                    amigos INTEGER DEFAULT '',
                    notificacoes TEXT DEFAULT '',
                    tarefas TEXT DEFAULT ''
                )''')

# Insere um usuário de dadologin no banco de dados
#cursor.execute("INSERT INTO usuarios (login, senha) VALUES (?, ?)", ("usuario1", "senha123"))

# Salva as alterações no banco de dados
conn.commit()

# Fecha a conexão com o banco de dados
conn.close()
def inserir_login(login, senha):
    try:
        conn = sqlite3.connect('dadologin.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (login, senha) VALUES (?, ?)", (login, senha))
        conn.commit()
        conn.close()
        text = "login salvo com sucesso"
        return text
    except:
        text = "erro de login"
        return text
    
def consultalogin(text):
    conn = sqlite3.connect('dadologin.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE login=?", (text,))
    resultado = cursor.fetchone()
    conn.close()
    if resultado:
        return resultado
    else:
        return "404"
    


            #num é o endero do banco, dado a informação
def alt_dado(num, id_user, dado, comando):
    conn = sqlite3.connect('dadologin.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios WHERE id=?", (id_user,))
    resultado = cursor.fetchone()

    lista =resultado[num]

    if comando == "add":
        lista = lista +" ??? "+ dado
    elif comando == "delete":
        dado = " ??? "+dado
        lista = lista.replace(dado,"")
    elif comando == "alt":
        lista = lista.replace(dado,("feito " +dado))
    if num == 5:
        cursor.execute("UPDATE usuarios SET amigos=? WHERE id=?", (lista, id_user))
    elif num == 6:
        cursor.execute("UPDATE usuarios SET notificacoes=? WHERE id=?", (lista, id_user))
    if num == 7:
        cursor.execute("UPDATE usuarios SET tarefas=? WHERE id=?", (lista, id_user))
    
    
    conn.commit()
    conn.close()
    return



def consulta(num):#########################
    conn = sqlite3.connect('dadologin.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE id=?", (num,))
    resultado = cursor.fetchone()
    conn.close()
    if resultado:
        return resultado
    else:
        return "404"

    
def deletarusuario(logim):
    try:
        conn = sqlite3.connect('dadologin.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM usuarios WHERE login=?", (logim,))
        conn.commit()
        conn.close()
        return "usuario deletado com sucesso"
    except:
        return "erro ao tentar apagar usuario"
    
def alt_acumulador(logim,num):
    conn = sqlite3.connect('dadologin.db')
    cursor = conn.cursor()
    dados = consultalogin(logim)
    if num > 0:
        num = num + dados[3]
    cursor.execute("UPDATE usuarios SET acumulador=? WHERE login=?", (num, logim))
    if dados[3] > 5:
        cursor.execute("UPDATE usuarios SET bloqueado=? WHERE login=?", (1, logim))
    conn.commit()
    conn.close()

