import pytest

from src.citas import calcular_copago


# Ejemplo de prueba (ya escrita para que vea el formato).
def test_particular_paga_todo():
    assert calcular_copago(100000, "particular") == 100000


# Prueba 1: "contributivo" paga el 10 %.
def test_contributivo_paga_diez_por_ciento():
    assert calcular_copago(100000, "contributivo") == 10000


# Prueba 2: "subsidiado" no paga nada.
def test_subsidiado_paga_cero():
    assert calcular_copago(100000, "subsidiado") == 0


# Prueba 3: valores inválidos lanzan ValueError.
def test_valor_negativo_lanza_error():
    with pytest.raises(ValueError):
        calcular_copago(-1, "particular")


def test_tipo_afiliado_desconocido_lanza_error():
    with pytest.raises(ValueError):
        calcular_copago(100000, "vip")


# Pruebas extra: borde y redondeo.
def test_valor_cero_es_valido():
    assert calcular_copago(0, "contributivo") == 0


def test_resultado_se_redondea_a_dos_decimales():
    # 10 % de 33333.33 = 3333.333 -> 3333.33
    assert calcular_copago(33333.33, "contributivo") == 3333.33
