# Bloque 5: métricas

## Métricas DORA (datos en `datos/despliegues.csv`, periodo de 28 días)
Hoja de cálculo con las fórmulas: `datos/metricas_DORA.xlsx`.

- Frecuencia de despliegue: 0,71 despliegues por día (20 despliegues / 28 días, aprox. 5 por semana)
- Lead time de cambios (mediana, en horas): 20 h
- Tasa de fallo de cambios: 20 % (4 fallos / 20 despliegues)
- Tiempo medio de recuperación (horas): 4,5 h (5 + 3 + 2 + 8 = 18 h en 4 fallos)

Hallazgos sobre los datos:
- Los 3 despliegues hechos en viernes (#3, #8 y #17) fallaron: 100 % de fallo en viernes frente a 1 fallo en 17 despliegues de otros días (aprox. 6 %). El otro fallo (#13) fue un sábado.
- El fallo más largo (8 h, #17) ocurrió en viernes: la recuperación cae en fin de semana.
- Observación sobre los datos: el despliegue #20 tiene fecha 2026-09-30, posterior al último día del periodo (2026-09-28). Se incluyó tal cual lo entrega el docente; sin él la mediana del lead time sigue siendo 20 h y la frecuencia sería 19/28 = 0,68 por día. Conviene confirmarlo con el docente.

## Cuatro métricas por enfoque
| Enfoque | Métrica | Qué atributo ISO 25010 respalda |
|---|---|---|
| Scrum | % de historias terminadas que cumplen la DoD al cierre del sprint | Adecuación funcional (Corrección funcional) |
| Kanban | Tiempo de ciclo (de "En desarrollo" a "Hecho") y cumplimiento de límites WIP | Mantenibilidad (Modificabilidad: capacidad de cambiar con rapidez) |
| XP | Cobertura de pruebas unitarias (meta ≥ 80 %) | Mantenibilidad (Capacidad de ser probado) |
| DevOps | Tasa de fallo de cambios (meta: bajar del 20 % actual) | Fiabilidad (Ausencia de fallos, Recuperabilidad) |
