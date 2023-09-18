import login
import Bancologin
def test_cadastro():
    retorno =login.cadastro_senha("antonio","lurdes","lurdes")
    assert retorno == "/n login em uso, favor tentar novamente/n"

def test_cadastro_caso_1():
    retorno =login.cadastro_senha("lurdes","lurdes","lurdes")
    assert retorno == "coloque pelo menos um numero na senha"

def test_cadastro_caso_2():
    retorno =login.cadastro_senha("lurdes","lurdes1","lurdes1")
    assert retorno == "coloque pelo menos um digito especial"

def test_cadastro_caso_3():
    retorno =login.cadastro_senha("lurdes","lurdes1#","lurdes1$")
    assert retorno == "senahs divergem"


def test_cadastro_caso_4():
    retorno =login.cadastro_senha("lurdes","lurdes1#","lurdes1#")
    assert retorno == "login salvo com sucesso"

def test_cadastro_caso_5():
    retorno = Bancologin.deletarusuario("lurdes")
    assert retorno == "usuario deletado com sucesso"