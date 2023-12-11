import Bancologin
def notifica(id_user):
    resposta = Bancologin.consulta(id_user)
    text = resposta[6].replace(" ??? ", "\n")
    print("\n", text)
    cod = input("deseja apagar tudo?(sim)")
    if cod == "sim":   
        Bancologin.alt_dado(6,id_user,"","deleteall")

    
