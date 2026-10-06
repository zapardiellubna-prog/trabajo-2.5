from m2_05_testing.ejemplo1 import suma
def test_suma_basica():
    assert suma(2,3) == 5
def test_suma_con_negativos():
    assert suma(-2,10) == 8