import login
import Bancologin

def test_ent_login():
    retorno = login.ent_login("joãoninguem","00")
    assert retorno == "senha ou login invalidos"


def test_ent_login_caso_2():
    Bancologin.inserir_login("antonio3","05")
    retorno = login.ent_login("antonio3","00")
    retorno = login.ent_login("antonio3","00")
    retorno = login.ent_login("antonio3","00")
    retorno = login.ent_login("antonio3","00")
    retorno = login.ent_login("antonio3","00")
    retorno = login.ent_login("antonio3","00")
    retorno = login.ent_login("antonio3","00")
    retorno = login.ent_login("antonio3","00")
    retorno = login.ent_login("antonio3","00")
    retorno = login.ent_login("antonio3","00")
    print(retorno)
    Bancologin.deletarusuario("antonio3")
    assert retorno == "usuario Bloqueado"

def test_ent_login_caso_3():
    Bancologin.inserir_login("maria","00")
    retorno = login.ent_login("maria","graca")
    Bancologin.deletarusuario("maria")
    assert retorno == "senha invalida"

def test_ent_login_caso_4():
    Bancologin.inserir_login("maria4","dolores")
    retorno = login.ent_login("maria4","dolores")
    assert retorno > 0
