import pytest
from agendamento_reunioes.validador_reuniao import validar_informacoes_reuniao

def test_base_should_validate():
    data = "15/11/2025"
    hora = "02:04"
    assunto = "Teste01"
    actual_response = validar_informacoes_reuniao(data=data, hora=hora, assunto=assunto)

def test_campo_vazio_should_raise_exception():
    data = "12/01/2025"
    hora = "12:33"
    assunto = ""
    with pytest.raises(Exception):
        validar_informacoes_reuniao(data=data, hora=hora, assunto=assunto)

def test_mes_invalido1_should_raise_exception():
    data = "12/13/2025"
    hora = "12:33"
    assunto = "Teste03"
    with pytest.raises(Exception):
        validar_informacoes_reuniao(data=data, hora=hora, assunto=assunto)

def test_hora_invalida1_should_raise_exception():
    data = "13/11/2025"
    hora = "12:60"
    assunto = "Teste04"
    with pytest.raises(Exception):
        validar_informacoes_reuniao(data=data, hora=hora, assunto=assunto)

def test_hora_invalida2_should_raise_exception():
    data = "13/11/2025"
    hora = "32:44"
    assunto = "Teste05"
    with pytest.raises(Exception):
        validar_informacoes_reuniao(data=data, hora=hora, assunto=assunto)

def test_zero_esquerda_should_validate():
    data = "05/01/2025"
    hora = "02:04"
    assunto = "Teste06"
    actual_response = validar_informacoes_reuniao(data=data, hora=hora, assunto=assunto)

def test_hora_invalida3_should_raise_exception():
    data = "13/11/2025"
    hora = "-22:44"
    assunto = "Teste07"
    with pytest.raises(Exception):
        validar_informacoes_reuniao(data=data, hora=hora, assunto=assunto)

def test_data_invalida1_should_raise_exception():
    data = "29/02/2025"
    hora = "-22:44"
    assunto = "Teste08"
    with pytest.raises(Exception):
        validar_informacoes_reuniao(data=data, hora=hora, assunto=assunto)