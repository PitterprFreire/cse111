
from endereco import extrair_cep, extrair_cidade, extrair_estado
import pytest

def test_extrair_cep():

    assert extrair_cep("Rua Pera Marmelo, 565, Vila Aurora, São Paulo - SP, 05185-420") == "05185-420"

def test_extrair_cidade():

    assert extrair_cidade("Rua Pera Marmelo, 565, Vila Aurora, São Paulo - SP, 05185-420") == "São Paulo"

def test_extrair_estado():

    assert extrair_estado("Rua Pera Marmelo, 565, Vila Aurora, São Paulo - SP, 05185-420") == "SP"

pytest.main(["-v", "--tb=line", "-rN", __file__])