from financas import cadastrar_divida, exibir_dividas
from banco_financas import inserir_no_banco, deletarusuario
import pytest

# valor da dívida deve ser menor de -0.01 ou acima de 0.01, com duas casas decimais
inserir_no_banco(0, "user0")
inserir_no_banco(1, "user1")

def test_0_should_raise_exception():
    user_id = 0
    divida_com = "user1"
    valor = "0.00"
    assunto = "assunto"
    with pytest.raises(Exception):
        cadastrar_divida(user_id, divida_com, valor, assunto)
        exibir_dividas(0)

def test_1_cent_should_validate():
    user_id = 0
    divida_com = "user1"
    valor = "0.01"
    assunto = "assunto"
    cadastrar_divida(user_id, divida_com, valor, assunto)

def test_negative_1_cent_should_validate():
    user_id = 0
    divida_com = "user1"
    valor = "-0.01"
    assunto = "assunto"
    cadastrar_divida(user_id, divida_com, valor, assunto)

def test_less_than_cent_should_raise_exception():
    user_id = 0
    divida_com = "user1"
    valor = "0.009"
    assunto = "assunto"
    with pytest.raises(Exception):
        cadastrar_divida(user_id, divida_com, valor, assunto)

def test_above_cent_should_raise_exception():
    user_id = 0
    divida_com = "user1"
    valor = "0.011"
    assunto = "assunto"
    with pytest.raises(Exception):
        cadastrar_divida(user_id, divida_com, valor, assunto)
    
deletarusuario("user0")
deletarusuario("user1")