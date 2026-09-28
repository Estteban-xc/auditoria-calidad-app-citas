# Cinco reglas de codificación del equipo

1. **Prueba primero (TDD):** ninguna función de negocio se implementa sin una prueba escrita antes que falle primero.
2. **Nombres claros en español y sin abreviaturas:** funciones en `snake_case` (`calcular_copago`), constantes en MAYÚSCULAS y variables que expliquen su contenido.
3. **Funciones pequeñas con una sola responsabilidad:** máximo 20 líneas por función, con *type hints* y *docstring* que describa la especificación.
4. **Fallar con claridad:** validar las entradas al inicio y lanzar excepciones específicas con mensaje (`ValueError`); nunca devolver valores silenciosos ni usar números mágicos (extraerlos a constantes).
5. **Integración pequeña y frecuente:** commits pequeños con mensaje descriptivo, todo cambio entra por Pull Request revisado, y `main` siempre debe tener el CI en verde.
