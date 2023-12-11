import notifica
import Bancologin
import comunidade

def tarefas(id_user):
    cod = True
    while cod:
        comando = input("\ndigite o numero da opção \n 1 tarefa para voce\n 2 tarefa para seu amigo\n 3 para Historico de tarefas\n 4 Tarefa executada\n 5 para excluir\n 6 para volta\n")
        if comando == "1":
            nova_tarefa(id_user)
        elif comando == "2":
            tarefa_amigo(id_user)
        elif comando == "3":
            historico_tarefa(id_user)
        elif comando == "4":
            tarefa_executada(id_user)
        elif comando == "5":
            excluir_tarefa(id_user)
        elif comando == "6":
            return
        else:
            print("erro de digitação")
        return


def nova_tarefa(id_user):
    cod2 = True
    while cod2:
        comando2 = input("\nfavor digite a tarefa\n")
        print("\nA tarefa é para vc e é ", comando2 , "digite sim para continual\n")
        comando3 = input()
        if comando3 == "sim":
            Bancologin.alt_dado(7,id_user,comando2,"add")
            Bancologin.alt_dado(6,id_user,comando2,"add")
            return

def tarefa_amigo(id_user):
    cod2 = True
    while cod2:
        comando2 = input("\nfavor didite a tarefa\n")
        resposta = Bancologin.consulta(id_user)
        lista = comunidade.lista_amigos(id_user)
        print(lista)
        comando4 = input("\n digite o nome do seu amigo\n")
        id_amigo =Bancologin.consultalogin(comando4)
        if id_amigo == "404":
            print("erro de digitação")
        else:
            print ("\nA tarefa é para seu amigo e é ", comando2 , "digite sim para continual\n")
            comando3 = input()
            if comando3 == "sim":
                Bancologin.alt_dado(7,id_amigo[0],comando2,"add")
                Bancologin.alt_dado(6,id_amigo[0],comando2,"add")
        return
                
def historico_tarefa(id_user):
    resposta = Bancologin.consulta(id_user)
    text=resposta[7]
    text = text.replace(" ??? ", "\n")
    print(text)
    return

def tarefa_executada(id_user):
    resposta = Bancologin.consulta(id_user)
    text=resposta[7]
    text = text.replace(" ??? ", "\n")
    cod = input("digite exatametne o nome da tarefa\n")
    resp = confere(text,cod)
    if resp == True:
        print("\ncomando confirmado\n")
    else:
        print("\nerro de digitação\n")   
    Bancologin.alt_dado(7,id_user,cod,"alt")
    print(text) 
    return

def excluir_tarefa(id_user):
    resposta = Bancologin.consulta(id_user)
    text=resposta[7]
    text = text.replace(" ??? ", "\n")
    print(text)
    cod = input("digite o nuome da tarefa")
    resp = confere(text,cod)
    if resp == True:
        print("\ncomando confirmado\n")
        Bancologin.alt_dado(7,id_user,cod,"delete")
    else:
        print("\nerro de digitação\n")
    return
            

def confere(dado, dado2):
    numero =dado.count(dado2)
    if numero > 0:
        return True
    else:
        return False
