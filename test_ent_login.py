import login

def test_ent_login():
    retorno = login.ent_login("joãoninguem","00")
    assert retorno == "senha ou login invalidos"


def test_ent_login_caso_2():
    retorno = login.ent_login("antonio","00")
    assert retorno == "usuario Bloqueado"

def test_ent_login_caso_3():
    retorno = login.ent_login("maria","graca")
    assert retorno == "senha invalida"

def test_ent_login_caso_4():
    retorno = login.ent_login("maria","dolores")
    assert retorno == 8
