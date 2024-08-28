X = 5
Y = 10

def test_meu_primeiro_teste():
    assert 1 == 1, 'Isto está errado'

def test_X_igual_Y():
    assert X == Y, 'Não estão iguais'

def test_X_diferente_Y(): 
    assert X != Y, 'Não estão diferentes'

def test_X_maior_que_Y():
    assert X > Y, 'X não é maior que Y'

def test_X_menor_que_Y():
    assert X < Y, 'X não é menor que Y'