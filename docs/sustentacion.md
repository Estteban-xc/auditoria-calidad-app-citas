# Plan de cumplimiento: guion de 3 minutos

**(0:00 – 0:30) El problema.**
Auditamos una startup de citas médicas que entrega cada 2 semanas, con defectos que llegan a producción, pruebas manuales y despliegues los viernes. Con sus datos simulados de 28 días, el diagnóstico es concreto: 20 despliegues, 4 fallaron, es decir 20 % de tasa de fallo. Y lo más llamativo: los tres despliegues de viernes fallaron.

**(0:30 – 1:00) Diagnóstico ISO/IEC 25010:2023.**
Los defectos escapados afectan la fiabilidad (ausencia de fallos); las pruebas manuales, la mantenibilidad (capacidad de ser probado); los viernes sin control, la recuperabilidad. Añadimos un riesgo de seguridad por tratarse de datos de pacientes.

**(1:00 – 1:45) Scrum y Kanban.**
Definimos una Definition of Done de 6 criterios verificables: revisión por pares, pruebas y cobertura ≥ 80 %, aceptación del PO, análisis de seguridad, plan de rollback con despliegue de lunes a jueves y cero defectos críticos abiertos. En el tablero limitamos el trabajo en curso: 3 en desarrollo y 2 en revisión, para terminar antes de empezar.

**(1:45 – 2:15) XP y DevOps.**
Aplicamos TDD: escribimos las pruebas de `calcular_copago` antes de implementarla y fijamos 5 reglas de codificación. El workflow de GitHub Actions ejecuta las pruebas en cada push y se pone en rojo si la cobertura baja del 80 %: es nuestra puerta de calidad.

**(2:15 – 2:50) Métricas y meta.**
Frecuencia de 0,71 despliegues por día, lead time mediano de 20 horas, 20 % de fallos y 4,5 horas de recuperación. Nuestra meta para el próximo mes: bajar el fallo de cambios por debajo del 10 %, y no volver a desplegar los viernes.

**(2:50 – 3:00) Cierre.**
La calidad no se declara, se demuestra con evidencia: un pipeline en verde, una DoD verificable y métricas que se miden cada sprint.
