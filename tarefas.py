import notifica
import Bancologin

def tarefas(id_user):
    cod = True
    while cod:
        comando = input("\ndigite o numero da opção \n 1 tarefa para voce\n 2 tarefa para seu amigo\n 3 para Historico de tarefas\n 4 Tarefa executada\n 5 para excluir\n 6 para volta\n")
        if comando == "1":
            cod2 = True
            while cod2:
                comando2 = input("\nfavor didite a tarefa")
                print ("\nA tarefa é para vc e é ", comando2 , "digite sim para continual\n")
                comando3 = input()
                if comando3 == "sim":
                    #notifica.insert_notifica(id_user, comando2)#################
                    Bancologin.alt_dado(7,id_user,comando2,"add")
                    return
        elif comando == "2":
            cod2 = True
            while cod2:
                print()
                comando2 = input("\nfavor didite a tarefa")

                resposta = Bancologin.consulta(id_user)
                lista = resposta[5]
                for i in range(lista):
                    print(i,lista[i])######################################
                comando4 = input("\n digite o numero do seu amigo",int)
                Bancologin.consultalogin(nome)
                nome = lista[comando4]
                responsta2 = Bancologin.consultalogin(nome)

                print ("\nA tarefa é para seu amigo e é ", comando2 , "digite sim para continual\n")
                comando3 = input()
                if comando3 == "sim":
                    notifica.insert_notifica(responsta2, comando2)
                    Bancologin.alt_dado(7,responsta2,comando2,"add")
                    return
        elif comando == "3":
            resposta = Bancologin.consulta(id_user)
            text=resposta[7]
            text = text.replace(" ??? ", "\n")
            print(text)
        elif comando == "4":
            resposta = Bancologin.consulta(id_user)
            text=resposta[7]
            text = text.replace(" ??? ", "\n")
            cod = input("digite exatametne o nome da tarefa")
            resp = confere(text,cod)
            if resp == True:
                print("\ncomando confirmado\n")
            else:
                print("\nerro de digitação\n")
            
            Bancologin.alt_dado(7,id_user,cod,"alt")
            print(text)
        elif comando == "5":
            resposta = Bancologin.consulta(id_user)
            text=resposta[7]
            text = text.replace(" ??? ", "\n")
            cod = input("digite o numero da tarefa")
            resp = confere(text,cod)
            if resp == True:
                print("\ncomando confirmado\n")
            else:
                print("\nerro de digitação\n")
            
            Bancologin.alt_dado(7,id_user,cod,"delete")
        elif comando == "6":
            return
        else:
            print("erro de digitação")
        return

def confere(dado, dado2):
    numero =dado.count(dado2)
    if numero > 0:
        return True
    else:
        return False