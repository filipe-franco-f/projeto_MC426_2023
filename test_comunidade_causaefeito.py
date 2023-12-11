import comunidade
import Bancologin
#mesmo 2 usuarios distinto que não se adicionaram são da mesma comunidade porque compartilham alguem em comum
def test_test_classe1():
    Bancologin.inserir_login("eduardo","01")
    Bancologin.inserir_login("eduardo1","01")
    Bancologin.inserir_login("eduardo2","01")
    Bancologin.inserir_login("eduardo3","01")
    vetor = Bancologin.consultalogin("eduardo")
    vetor1 = Bancologin.consultalogin("eduardo3")
    comunidade.add_amigo(vetor[0],"eduardo")
    comunidade.add_amigo(vetor[0],"eduardo3")
    comunidade.add_amigo(vetor[0],"eduardo2")
    comunidade.add_amigo(vetor[0],"eduardo1")
    comunidade.atualizaramg(vetor[0],vetor1[0])
    resposta = comunidade.add_amigo(vetor1[0],"eduardo1")
    Bancologin.deletarusuario("eduardo1")
    Bancologin.deletarusuario("eduardo2")
    Bancologin.deletarusuario("eduardo3")
    Bancologin.deletarusuario("eduardo")
    assert resposta == "ja é amigo"
    

def test_test_classe2():
    Bancologin.inserir_login("eduardo","01")
    Bancologin.inserir_login("eduardo1","01")
    vetor = Bancologin.consultalogin("eduardo")
    resposta = comunidade.add_amigo(vetor[0],"eduardo1")
    Bancologin.deletarusuario("eduardo")
    Bancologin.deletarusuario("eduardo1")
    assert resposta == "amigo encontrado"

def test_test_classe3():
    Bancologin.inserir_login("eduardo","01")
    Bancologin.inserir_login("eduardo1","01")
    vetor = Bancologin.consultalogin("eduardo")
    resposta = comunidade.add_amigo(vetor[0],"eduardo1")
    resposta = comunidade.add_amigo(vetor[0],"eduardo1")
    Bancologin.deletarusuario("eduardo")
    Bancologin.deletarusuario("eduardo1")
    assert resposta == "ja é amigo"

def test_test_classe4():
    Bancologin.inserir_login("eduardo","01")
    vetor = Bancologin.consultalogin("eduardo")
    resposta = comunidade.add_amigo(vetor[0],"eduardo1")
    Bancologin.deletarusuario("eduardo")
    assert resposta == "amigo não encontrado"