import pytest
from m2_05_testing.ejemplo2 import dividir
def test_dividir_ok():
    assert dividir(10,2) == 5
def test_dividir_por_cero_lanza_error():
    with pytest.raises(ValueError):
        dividir(10,0)