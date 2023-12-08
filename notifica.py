import Bancologin
def insert_notifica(id_user,msg):
    resposta = Bancologin.consulta(id_user)
    return

def notifica(id_user):
    resposta = Bancologin.consulta(id_user)
    print("\n", resposta[5])
    