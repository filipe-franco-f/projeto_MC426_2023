from agendamento import agendar_reuniao
from banco_agendamento import inserir_no_banco, deletarusuario
from datetime import datetime, timedelta
import pytest

# data de reuniao a ser agendada não pode ser antes do dia e horário atual
inserir_no_banco(0, "user0")

def test_before_current_time():
    user_id = 0
    data_hora_anterior = datetime.now() + timedelta(minutes=-1)
    data = f"{data_hora_anterior.day}/{data_hora_anterior.month}/{data_hora_anterior.year}"
    hora = f"{data_hora_anterior.hour}:{data_hora_anterior.minute}"
    assunto = "assunto"
    with pytest.raises(Exception):
        agendar_reuniao(user_id, data, hora, assunto)

def test_current_time():
    user_id = 0
    data_hora_atual = datetime.now()
    data = f"{data_hora_atual.day}/{data_hora_atual.month}/{data_hora_atual.year}"
    hora = f"{data_hora_atual.hour}:{data_hora_atual.minute}"
    assunto = "assunto"
    agendar_reuniao(user_id, data, hora, assunto)


deletarusuario("user0")
