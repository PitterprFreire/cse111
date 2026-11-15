
from nomes import criar_nome_completo, extrair_primeiro_nome, extrair_sobrenome
import pytest

def test_criar_nome_completo():

    assert criar_nome_completo("Pitter-Pinheiro-Ramalho","Freire") =="Freire; Pitter-Pinheiro-Ramalho"
    assert criar_nome_completo("Helena-Lopes","Freire") =="Freire; Helena-Lopes"
    assert criar_nome_completo("Juliana-Helena-Lopes","Freire") =="Freire; Juliana-Helena-Lopes"

def test_extrair_primeiro_nome():

    assert extrair_primeiro_nome("Freire; Pitter") =="Pitter"
    assert extrair_primeiro_nome("Freire; Helena") =="Helena"
    assert extrair_primeiro_nome("Freire; Juliana") =="Juliana"

def test_extrair_sobrenome():

    assert extrair_sobrenome("Freire; Pitter") =="Freire"
    assert extrair_sobrenome("Freire; Helena") =="Freire"
    assert extrair_sobrenome("Freire; Juliana") =="Freire"


pytest.main(['-v', "--tb=line", "-rN", __file__])
     