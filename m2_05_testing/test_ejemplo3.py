Parametrizar = "una misma prueba con muchas entradas."
import pytest
from m2_05_testing.ejemplo3 import es_par
@pytest.mark.parametrize(
    "n,esperado",
    [
        (0,True),
        (1,False),
        (2,True),
        (11,False),
        (-4,True),
    ],
)
def test_es_par(n,esperado):
    assert es_par(n) is esperado