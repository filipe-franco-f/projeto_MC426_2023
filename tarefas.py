import notifica
import Bancologin

def tarefas(id_user):
    cod = True
    while cod:
        comando = input("\ndigite o numero da opção \n 1 tarefa para voce\n 2 tarefa para seu amigo\n 3 para Historico de tarefas\n Tarefa executada\n 5 para volta")
        if comando == "1":
            cod2 = True
            while cod2:
                comando2 = input("\nfavor didite a tarefa")
                print ("\nA tarefa é para vc e é ", comando2 , "digite sim para continual\n")
                comando3 = input()
                if comando3 == "sim":
                    notifica.insert_notifica(id_user, comando2)
                    Bancologin.alt_acumulador(7,id_user,comando2,"add")
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
                    Bancologin.alt_acumulador(7,responsta2,comando2,"add")
                    return
        elif comando == "3":
            resposta = Bancologin.consulta(id_user)
            print(resposta[7])
        elif comando == "5":
            #################excluir tarefa
            resposta = Bancologin.consulta(id_user)
            lista = resposta[7]
            for i in range(lista):
                print(i,lista[i])######################################
            cod = input("digite o numero da tarefa")
            Bancologin.alt_acumulador(7,id_user,cod,"remove")
        elif comando == "6":
            return
        else:
            print("erro de digitação")
        return
        