import banco_agendamento
import agendamento_reunioes.validador_reuniao
from agendamento_reunioes.agendamento_exceptions import CampoVazioException, DataInvalidaException, reuniaoNaoEncontrada

class CampoVazioException(Exception):
    pass

class ValorInvalidoException(Exception):
    pass

# Função para agendar uma reunião
def agendar_reuniao(id_user, data, hora, assunto):
    try:
        data_hora = agendamento_reunioes.validador_reuniao.validar_informacoes_reuniao(data=data, hora=hora, assunto=assunto)
    except CampoVazioException:
        print("Erro: Preencha todos os campos.")
        raise CampoVazioException
    except DataInvalidaException:
        print("Erro: Formato de data/hora inválido.")
        raise DataInvalidaException
    except:
        print("Ocorreu um Erro.")
        return

    # Adiciona a reunião agendada à lista
    try:
        cadastro = banco_agendamento.cadastra_reuniao(id_user, data_hora.strftime('%d/%m/%Y %H:%M'), assunto)
    except:
        print("Erro: Erro ao agendar reuniao.")
        return

    print("Reunião agendada com sucesso.")


def desmarcar_reuniao(id_user, data, hora, assunto):
    try:
        data_hora = agendamento_reunioes.validador_reuniao.validar_informacoes_reuniao(data=data, hora=hora, assunto=assunto)
    except CampoVazioException:
        print("Erro: Preencha todos os campos.")
        return
    except DataInvalidaException:
        print("Erro: Formato de data/hora inválido.")
        return
    except:
        return

    try:
        cadastro = banco_agendamento.deletar_reuniao(id_user, data_hora.strftime('%d/%m/%Y %H:%M'), assunto)
    except reuniaoNaoEncontrada:
        print("Erro: Reunião não encontrada.")
        return
    except:
        print("Ocorreu um Erro")
        return

    print("Reunião deletada com sucesso.")


# Função para exibir as reuniões agendadas
def exibir_reunioes(id_user):
    reunioes_agendadas = banco_agendamento.checar_reunioes(id_user)
    if not reunioes_agendadas:
        print("Não há reuniões agendadas.")
    else:
        lista_reunioes = "\n".join([f"""Data: {data}\n Assunto: {assunto}\n ===============""" for data, assunto in reunioes_agendadas])
        print("Reuniões Agendadas:\n", lista_reunioes)

def handle_agendar_reuniao(id_user):
    data = input("Data (dd/mm/yyyy): ")
    hora = input("Hora (hh:mm): ")
    assunto = input("Assunto: ")
    agendar_reuniao(id_user, data, hora, assunto)

def handle_desmarcar_reuniao(id_user):
    data = input("Data (dd/mm/yyyy): ")
    hora = input("Hora (hh:mm): ")
    assunto = input("Assunto: ")
    desmarcar_reuniao(id_user, data, hora, assunto)

def agenda(id_user):
    while True:
        print("Digite uma das opçẽos: \n Agendar reunião\n Desmarcar reunião\n Exibir reuniões \n Voltar")
        comando = input()

        if comando == "agendar reuniao" or comando == "Agendar reuniao" or comando == "Agendar reunião" or comando == "agendar reunião":
            handle_agendar_reuniao(id_user)
        
        if comando == "desmarcar reuniao" or comando == "Desmarcar reuniao" or comando == "Desmarcar reunião" or comando == "desmarcar reunião":
            handle_desmarcar_reuniao(id_user)

        if comando == "exibir reuniões" or comando == "Exibir reuniões" or comando == "exibir reunioes" or comando == "Exibir reunioes":
            exibir_reunioes(id_user)

        if comando == "Voltar" or comando == "voltar":
            return
        print("\n")