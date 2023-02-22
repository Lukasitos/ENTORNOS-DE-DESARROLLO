lista = list(range(6))

cadena = "esto es una cadena"

print(lista[1:-1])
print(lista[0:-2])

print(cadena[4:-5])
print(cadena[5:len(cadena)])


def conjuga(verbo):
    sol = []
    raiz = verbo[0:4]
    termi= verbo[4:len(verbo)]
    listar = ['o', 'as', 'a', 'amos', 'áis', 'an']
    if termi == "ar":
        for i in listar:
            sol.append(raiz+i)
    return sol
print(conjuga("cantar"))


import pytest

@pytest.mark.basic
def test_notas():
    assert "notable" == test_notas(8)
    assert "notable" == test_notas(3)
    assert "sobresaliente" == test_notas(10)
    assert "suspenso" == test_notas(3)
    assert "suspenso" == test_notas(-3)
    assert "bien" == test_notas(6)
    assert "la nota introducida es erronea" == test_notas(24)
