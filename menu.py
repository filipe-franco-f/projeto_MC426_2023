import login
import notifica
import tarefas
import Bancologin
import comunidade
import financas
import agendamento
id_user = 0
name_user = "user"
def sobre():
    print("\nEste é um aplicativo feito por Alunos da unicamp para o curso de engengharia de software\n")
    return
while id_user == 0:
    print("Por favor digite o Comando entre: \n Login \n Sobre")
    comando = input()
    if comando=="Login" or comando=="login":
        resposta = login.login()
        print(resposta)
        try:
            confere = Bancologin.consulta(resposta)
            if confere == "404":
                id_user = 0
            else:
                id_user = resposta
                name_user = confere[1]
        except:
            id_user = 0
    elif comando=="Sobre" or comando=="sobre":
        sobre()
    else:
        print("Comando Invalido")


while True:
    print("\nBem vindo ", name_user,"\n Digite uma das opçẽos: \n Notificação\n Agenda\n Tarefas\n Comunidade\n Finanças\n Logoff\n")
    comando = input()
    if comando == "nofificacao" or comando == "notificação" or comando == "Notificação":
        notifica.notifica(id_user)
    elif comando == "agenda" or comando == "Agenda":
        agendamento.agenda(id_user)
    elif comando == "Finanças" or comando == "finanças" or comando == "financas":
        financas.administrar_financas(id_user)
    elif comando == "Tarefas" or comando == "tarefas":
        tarefas.tarefas(id_user)
    elif comando == "Comunidade" or comando == "comunidade":
        comunidade.inicio(id_user)
    elif comando == "logoff" or comando == "Logoff":
        id_user = 0
        break
    else:
        print("\n Comando Invalido")
print("Logout efetuado com sucesso")
