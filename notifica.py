import Bancologin
def insert_notifica(id_user,msg):
    resposta = Bancologin.consulta(id_user)
    Bancologin.alt_acumulador(7,id_user,msg,"add")
    return

def remove_notifica(id_user,msg):
    resposta = Bancologin.consulta(id_user)
    Bancologin.alt_acumulador(7,id_user,msg,"remove")
    return

def notifica(id_user):
    resposta = Bancologin.consulta(id_user)
    text = resposta[6].replace(" ??? ", "\n")
    print("\n", text)
    cod = input("deseja apagar tudo?(sim)")
    if cod == "sim":   
        Bancologin.alt_dado(6,id_user,"","deleteall")

    