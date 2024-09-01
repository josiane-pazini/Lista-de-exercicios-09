# 1- Bibliotecas, frameworks e referencias externas
import pytest

from area.area import area_quadrado, area_retangulo, area_triangulo
from utils.utils import ler_csv

# 2- Testes

def test_area_quadrado():

    l = 3
    resultado_esperado = 9
    resultado_obtido = area_quadrado(l)
    assert resultado_esperado == resultado_obtido 

def test_area_retangulo():

    b = 3
    h = 2
    resultado_esperado = 6
    resultado_obtido = area_retangulo(b, h)
    assert resultado_esperado == resultado_obtido 

def test_area_triangulo():
    
    b = 3
    h = 2
    resultado_esperado = 3
    resultado_obtido = area_triangulo(b, h)
    assert resultado_esperado == resultado_obtido 


#Teste baseados em Dados = Data Driven Tests (DDT) --> massa de teste
#3- Teste com massa de valores no formato de lista
@pytest.mark.parametrize('b, h, resultado_esperado', 
                         [
                             (7, 2, 14),
                             (3, 1.5, 4.5),
                             (10, 5, 50),
                             (2.25, 1.75, 3.9375 ),
                             (10, 0, 0)
                         ]
                         )
def test_area_retangulo_lista(b, h, resultado_esperado):

    resultado_obtido = area_retangulo(b, h)
    assert resultado_esperado == resultado_obtido 


@pytest.mark.parametrize('b, h, resultado_esperado',
                            ler_csv('./fixtures/massa_area.csv')
                         )

def test_area_retangulo_csv(b, h, resultado_esperado):

    resultado_obtido = area_retangulo(float(b), float(h))
    assert float(resultado_esperado) == resultado_obtido 
