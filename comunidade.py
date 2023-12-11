import Bancologin

def inicio(id_user):
    w = Bancologin.consulta(id_user)
    add_amigo(id_user,w[1])

    a = lista_amigos(id_user)
    print(a)
    resp = input("Deseja add usuario a comunidade?(sim)\n")
    if resp == "sim":
        amigo = input("Digite o login do novo user\n")
        add_amigo(id_user,amigo

    resp = input("deseja atualizar amigos?(sim)")
    n = len(a)
    if resp == "sim":
        for i in range(n):
            p = str(a[i])
            vetor = Bancologin.consultalogin(p)
            atualizaramg(id_user,vetor[0])


def add_amigo(id_user,amigo):
    
    resposta = Bancologin.consultalogin(amigo)
    if resposta == "404":
        return "amigo não encontrado"
    else:
        verifica = Bancologin.consulta(id_user)
        v = verifica[5]
        t = confere(v,amigo)
        if t == True:
            print("ja é amigo")
        else:
            atualizaramg(id_user,resposta[0])
            Bancologin.alt_dado(5,id_user,amigo,"add")
            Bancologin.alt_dado(6,id_user,("novo amigo user "+amigo),"add")
            return "amigo encontrado"
    
def lista_amigos(id_user):
    resp=Bancologin.consulta(id_user)
    dado = resp[5]
    dado = dado.replace(" ??? "," ")
    dado = dado.split()
    return dado

def atualizaramg(id_user,amigo_id):
    dado1 = lista_amigos(id_user)
    dado2 = lista_amigos(amigo_id)
    d1 = list(set(dado1).difference(dado2))
    d2 = list(set(dado2).difference(dado1))
    print(d1,"\n",d2)
    y =len(d1)
    for i in range(y):
        p = str(d1[i])
        Bancologin.alt_dado(5,amigo_id,p,"add")
    y =len(d2)
    for i in range(y):
        p = str(d2[i])
        Bancologin.alt_dado(5,id_user,p,"add")
    return d1,d2

def confere(dado, dado2):
    numero =dado.count(dado2)
    if numero > 0:
        return True
    else:
        return False