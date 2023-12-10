import login
import agendamento_reunioes.agendamento as agen
import notifica
import tarefas


id_user = 0
name_user = "user"
def sobre():
    print("\nEste é um aplicativo feito por Alunos da unicamp para o curso de engengharia de software\n")
    return
while id_user == 0:
    print("Por favor digite o Comando entre: \n Login: \n Sobre:")
    comando = input()
    if comando=="Login" or comando=="login":
        resposta = login.login()
        id_user = resposta[0]
    #elif comando == "cadastro" or comando == "cadadstro":
    #    login.cadastro_senha()
    elif comando=="Sobre" or comando=="sobre":
        sobre()
    else:
        print("Comando Invalido")
while True:
    print("\n Bem vindo ", name_user,"\n Digite uma das opçẽos: \n Notificação\n Agenda\n Tarefas\n Logoff\n")
    comando = input()
    if comando == "agenda" or comando == "agenda":
        agen.agendar_com_interface(id_user)
    elif comando == "nofificacao" or comando == "notificação" or comando = "Notificação"
        notifica.notifica(id_user)
    elif comando == "Tarefas" or comando == "tarefas":
        tarefas.tarefas(id_user)
    elif comando == "logoff" or comando == "Logoff":
        id_user = 0
        break
    else:
        print("\n Comando Invalido" )
print("Logout efetuado com sucesso")