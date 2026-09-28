"""Módulo de citas médicas (código base del taller)."""

PORCENTAJE_COPAGO = {
    "contributivo": 0.10,
    "subsidiado": 0.0,
    "particular": 1.0,
}


def calcular_copago(valor_consulta: float, tipo_afiliado: str) -> float:
    """Calcula el copago que paga el paciente.

    Especificación:
    - "contributivo": paga el 10 % del valor de la consulta.
    - "subsidiado": paga 0.
    - "particular": paga el 100 %.
    - Si valor_consulta es negativo, lanza ValueError.
    - Si tipo_afiliado no es uno de los tres anteriores, lanza ValueError.
    - El resultado se redondea a 2 decimales.
    """
    if valor_consulta < 0:
        raise ValueError("El valor de la consulta no puede ser negativo")
    if tipo_afiliado not in PORCENTAJE_COPAGO:
        raise ValueError(f"Tipo de afiliado no válido: {tipo_afiliado!r}")
    return round(valor_consulta * PORCENTAJE_COPAGO[tipo_afiliado], 2)
