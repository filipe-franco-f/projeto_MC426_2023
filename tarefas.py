import notifica

def tarefas(user_id):
    cod = True
    while cod:
        comando = input("\ndigite o numero da opção \n 1 tarefa para voce\n 2 tarefa para seu amigo\n 3 para volta"
        if comando == "1":
            cod2 = True
            while cod2:
                comando2 = input("\nfavor didite a tarefa")
                print ("\nA tarefa é para vc e é ", comando2 , "digite sim para continual\n")
                comando3 = input()
                if comando3 == "sim":
                    notifica.insert_notifica(id_user, comando2)
                    return
        elif comando == "2":
            cod2 = True
            while cod2:
                print()
                comando2 = input("\nfavor didite a tarefa")
                comando4 = input("\n digite o nome do seu amigo")
                print ("\nA tarefa é para seu amigo e é ", comando2 , "digite sim para continual\n")
                comando3 = input()
                if comando3 == "sim":
                    notifica.insert_notifica(id_user, comando2)
                    return
        elif comando == "3":
            return
        else
            print("erro de digitação")