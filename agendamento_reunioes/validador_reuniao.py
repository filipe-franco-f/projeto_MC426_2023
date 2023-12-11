from datetime import datetime
from agendamento_reunioes.agendamento_exceptions import (
    CampoVazioException,
    DataInvalidaException
)

def validar_informacoes_reuniao(data: str, hora:str, assunto:str):
    if not data or not hora or not assunto:
        raise CampoVazioException

    # Formata a data e hora
    data_hora = f"{data} {hora}"

    # Converte a data e hora para um objeto datetime
    try:
        data_hora = datetime.strptime(data_hora, "%d/%m/%Y %H:%M")
    except ValueError:
        raise DataInvalidaException

    return data_hora