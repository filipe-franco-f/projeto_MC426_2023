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
    
    # queremos data e hora atual sem informação de unidades menores que minuto
    data_hora_atual = datetime.now()
    data_atual = f"{data_hora_atual.day}/{data_hora_atual.month}/{data_hora_atual.year}"
    hora_atual = f"{data_hora_atual.hour}:{data_hora_atual.minute}"
    data_hora_atual = datetime.strptime(f"{data_atual} {hora_atual}", "%d/%m/%Y %H:%M") 
    try:
        data_hora = datetime.strptime(data_hora, "%d/%m/%Y %H:%M")
    except:
        raise DataInvalidaException
    if data_hora < data_hora_atual:
        raise DataInvalidaException

    return data_hora