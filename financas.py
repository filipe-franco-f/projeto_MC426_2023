import banco_financas
from banco_financas import DbParams

class CampoVazioException(Exception):
    pass

class ValorInvalidoException(Exception):
    pass

def validar_informacoes_divida(pessoa: str, valor:str, assunto:str):
    if not pessoa or not valor or not assunto:
        raise CampoVazioException

    # Converte a data e valor para um objeto datetime
    if len(valor) < 4 or valor[-3] != ".":
        raise ValorInvalidoException
    try:
        reais = int(valor[:-3])
        centavos = int(valor[-2:])
    except:
        raise ValorInvalidoException

    return 

def cadastrar_divida(id_user, pessoa, valor, assunto):
    try:
        validar_informacoes_divida(pessoa=pessoa, valor=valor, assunto=assunto)
    except CampoVazioException:
        print("Erro: Preencha todos os campos.")
        return
    except ValorInvalidoException:
        print("Erro: Formato de valor da dívida inválido.")
        return
    except:
        return
    db_params_user1 = DbParams(id_user, None, valor, assunto)
    db_params_user2 = DbParams(None, pessoa, None, None)

    try:
        fill = banco_financas.cadastra_divida(db_params_user1, db_params_user2)
    except:
        print("Erro: Pessoa não encontrada.")
        return

    print("Dívida cadastrada com sucesso.")


def quitar_divida(id_user, pessoa, valor, assunto):
    try:
        validar_informacoes_divida(pessoa=pessoa, valor=valor, assunto=assunto)
    except CampoVazioException:
        print("Erro: Preencha todos os campos.")
        return
    except ValorInvalidoException:
        print("Erro: Formato de valor da dívida inválido.")
        return
    except:
        print("Ocorreu um Erro.")
        return
    
    db_params_user1 = DbParams(id_user, None, valor, assunto)
    db_params_user2 = DbParams(None, pessoa, None, None)

    try:
        fill = banco_financas.quitar_divida(db_params_user1, db_params_user2)
    except banco_financas.PessoaNaoEncontrada:
        print("Erro: Pessoa não encontrada.")
        return
    except banco_financas.DividaNaoEncontrada:
        print("Erro: Dívida não encontrada.")
        return
    except:
        print("Ocorreu um Erro.")
        return

    print("Dívida quitada com sucesso.")

# Função para exibir as dividas
def exibir_dividas(id_user):
    dividas = banco_financas.checar_dividas(id_user)
    if not dividas:
        print("Não há dívidas cadastradas.")
    else:
        lista_dividas = "\n".join(
            [f"""Pessoa: {pessoa}\n Valor: {valor}\n Assunto: {assunto}\n ===============""" for pessoa, valor, assunto in dividas])
        print("Dívidas:\n", lista_dividas)

def handle_cadastrar_divida(id_user):
    pessoa = input("Divida com usuário: ")
    valor = input("Valor da dívida (x.xx): ")
    assunto = input("Motivo da dívida: ")
    cadastrar_divida(id_user, pessoa, valor, assunto)

def handle_quitar_divida(id_user):
    pessoa = input("Divida com usuário: ")
    valor = input("Valor da dívida (x.xx): ")
    assunto = input("Motivo da dívida: ")
    quitar_divida(id_user, pessoa, valor, assunto)

def administrar_financas(id_user):
    while True:
        print("Digite uma das opçẽos: \n Cadastrar divida\n Quitar divida\n Exibir dividas \n Voltar")
        comando = input()

        if comando == "cadastrar divida" or comando == "Cadastrar divida" or comando == "cadastrar dívida" or comando == "Cadastrar dívida":
            handle_cadastrar_divida(id_user)
        
        if comando == "quitar divida" or comando == "Quitar divida" or comando == "quitar dívida" or comando == "Quitar dívida":
            handle_quitar_divida(id_user)

        if comando == "exibir dividas" or comando == "Exibir dividas" or comando == "exibir dívidas" or comando == "Exibir dívidas":
            exibir_dividas(id_user)

        if comando == "Voltar" or comando == "voltar":
            return
        print("\n")