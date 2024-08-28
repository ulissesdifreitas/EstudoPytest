from pytest import mark
from codigo.jogo import brincadeira

"""
O teste é formado por 3 etapas: (GWT - AAA)
- GIVEN - Dado que
- WHEN - Quando 
- THEN - Então

- ARANGE
- ACT
- ASSERT

xUnit Patterns - Gerard Mezaros
"Um teste é composto por 4 passos"

- Setup - Dado
- Exercise - Quando
- Verify - Então
- TearDown - "Desmonta tudo antes que seja tarde".

"""

def test_quando_bricadeira_receber_1_entao_deve_retornar_1():
    entrada = 1   #dado 
    esperado = 1  #dado
 
    resultado = brincadeira(entrada) #quando

    assert resultado == esperado  #então
    
def test_quando_bricadeira_receber_2_entao_deve_retornar_2():
    # TDD - Kent Beck - One-step Test
    assert brincadeira(2) == 2

def test_quando_bricadeira_receber_3_entao_deve_retornar_queijo():
    # TDD - Kent Beck - One-step Test
    assert brincadeira(3) == 'queijo'

@mark.goiabada
def test_quando_bricadeira_receber_5_entao_deve_retornar_goiabada():
    # TDD - Kent Beck - One-step Test
    assert brincadeira(5) == 'goiabada'

@mark.goiabada
def test_quando_bricadeira_receber_10_entao_deve_retornar_goiabada():
    # TDD - Kent Beck - One-step Test
    assert brincadeira(10) == 'goiabada'

@mark.goiabada
def test_quando_bricadeira_receber_20_entao_deve_retornar_goiabada():
    # TDD - Kent Beck - One-step Test
    assert brincadeira(20) == 'goiabada'

@mark.skip(reason='Not implemented')
def test_quando_bricadeira_receber_VALOR_NEGATIVO_entao_deve_retornar_None():
    # TDD - Kent Beck - One-step Test
    assert brincadeira(20) == 'goiabada'

@mark.parametrize(
    'entrada',
    [5, 10, 20, 25, 35]
)
def test_bricadeira_deve_retornar_goiaba_com_multiplos_de_5(entrada):
    # TDD - Kent Beck - One-step Test
    assert brincadeira(entrada) == 'goiabada'


@mark.parametrize(
    'entrada',
    [3, 6, 9, 12, 18]
)
def test_bricadeira_deve_retornar_queijo_com_multiplos_de_3(entrada):
    # TDD - Kent Beck - One-step Test
    assert brincadeira(entrada) == 'goiabada'

# @mark.parametrizado
# @mark.parametrize(
#     'entrada',
#     [(1, 1), (2, 2), (3, 'queijo'), (4, 4), (5, 'goiabada')]
# )
# def test_bricadeira_deve_retornar_valor_esperado(entrada, esperado):
#     # TDD - Kent Beck - One-step Test
#     assert brincadeira(entrada) == esperado

@mark.xfail
def test_xfail():
    # TDD - Kent Beck - One-step Test
    assert brincadeira(20) == 'goiabada'