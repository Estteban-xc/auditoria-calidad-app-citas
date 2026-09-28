# Bloque 1: problemas del caso y atributos ISO/IEC 25010:2023

Atributos: adecuación funcional, eficiencia de desempeño, compatibilidad, capacidad de interacción, fiabilidad, seguridad, mantenibilidad, flexibilidad, seguridad operacional (safety).

| Problema del caso | Atributo afectado | Subcaracterística | Métrica propuesta |
|---|---|---|---|
| Defectos que llegan a producción | Fiabilidad (secundario: Adecuación funcional) | Ausencia de fallos; Corrección funcional | Defectos escapados por release; tasa de fallo de cambios (fallos / despliegues) |
| Pruebas solo manuales | Mantenibilidad | Capacidad de ser probado | % de cobertura de pruebas automatizadas; horas de regresión manual por release |
| Despliegues los viernes sin control | Fiabilidad | Recuperabilidad (y Disponibilidad) | Tasa de fallo por día de despliegue; tiempo medio de recuperación (MTTR) |
| Datos de pacientes en una app de salud sin controles de seguridad definidos (riesgo inferido del contexto) | Seguridad | Confidencialidad; Integridad | Vulnerabilidades altas/críticas abiertas; secretos detectados en el repositorio |

Nota: en la versión 2023 de la norma "Usabilidad" pasó a llamarse *Capacidad de interacción*, "Portabilidad" a *Flexibilidad*, y se añadió *Seguridad operacional (safety)*.
