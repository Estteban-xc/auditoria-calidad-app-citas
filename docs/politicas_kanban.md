# Tablero Kanban: políticas por columna

Enlace o captura del tablero: _______ (pegue aquí el enlace de Trello / GitHub Projects y suba la captura como `docs/tablero.png`)

Los límites WIP están calculados para un equipo de 3 a 4 personas: aproximadamente 1 tarjeta por persona en desarrollo, y colas cortas hacia adelante.

| Columna | Límite WIP | Política de entrada | Política de salida |
|---|---|---|---|
| Por hacer | 6 | Historia priorizada por el PO, con criterios de aceptación escritos y estimada | Alguien del equipo tiene capacidad libre y toma la tarjeta más prioritaria |
| En desarrollo | 3 | Rama creada; las pruebas se escriben antes que el código (TDD) | Pull Request abierto, pruebas locales en verde |
| En revisión / pruebas | 2 | PR abierto y CI ejecutándose; hay un revisor asignado | PR aprobado, CI en verde (pruebas + cobertura ≥ 80 %) y criterios de aceptación verificados |
| Listo para desplegar | 2 | Cumple los criterios 1 a 4 de la DoD y tiene plan de rollback | Desplegado en producción en ventana lunes–jueves (nunca viernes) |
| Hecho | Sin límite | Desplegado y sin alertas en las primeras 24 h | — (se archiva al cierre del sprint) |

Reglas generales: si una columna llega a su límite WIP, no se toma trabajo nuevo; se ayuda a desbloquear lo que ya está en curso. Una tarjeta que lleve más de 3 días en la misma columna se revisa en la daily.
