import getpass
import Bancologin
import banco_financas
import banco_agendamento
def verifica_caracteres(texto, caracteres):
    caracteres_presentes = [caractere for caractere in caracteres if caractere in texto]
    
    if caracteres_presentes:
        return "ok"
    else:
        return "erro"

def ent_login(logim, senha):
    retorno = Bancologin.consultalogin(logim)
    #print(retorno)
    if retorno == "404":
        return "senha ou login invalidos"
    elif retorno[4] == 1:
        return "usuario Bloqueado"
    elif senha != retorno[2]:
        Bancologin.alt_acumulador(logim, 1)
        return "senha invalida"
    else:
        Bancologin.alt_acumulador(logim, 0)
        print("login efetuado")
        return retorno[0]

def cadastro_senha(logim, senha, senha2):
    resposta = Bancologin.consultalogin(logim)
    if resposta == "404":
        caracteres = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        resultado = verifica_caracteres(senha, caracteres)
        caracteres2 = ['!', '@', '#', '$', '%', '?', '&', '(', ')', '-', '|', '}', '{']
        resultado2 = verifica_caracteres(senha, caracteres2)
        if resultado == "erro":
            return "coloque pelo menos um numero na senha"
        elif resultado2 == "erro":
            return "coloque pelo menos um digito especial"
        elif senha != senha2:
            return "senahs divergem"
        else:
            resposta = Bancologin.inserir_login(logim,senha)
            id = Bancologin.consultalogin(logim)
            banco_financas.inserir_no_banco(id[0] ,logim)
            banco_agendamento.inserir_no_banco(id[0], logim)
            return resposta
    else:
        return "\n login em uso, favor tentar novamente\n"
            

def login():
    comando = input("digite '1' para entrar com seu login ou '2' para se cadastrar\n")
    if comando == "1":
        texto = input("login: ")
        logim = texto
        senha = getpass.getpass("senha: ")
        resposta = ent_login(logim, senha)
        return resposta


    elif comando == "2":
        logim = input("digite login desejado: ")
        senha = getpass.getpass("digite a senha desejada: (precisa conter pelo menos um numero e um caracter em especial)") 
        senha2 = getpass.getpass("repita a senha")
        resposta = cadastro_senha(logim,senha,senha2)
        return resposta
    else:
        print("comando nao aceito")
        return 0