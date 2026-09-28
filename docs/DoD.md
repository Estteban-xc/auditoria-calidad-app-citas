# Definition of Done (6 criterios)

Cada criterio debe ser verificable (sí/no) y estar ligado a un atributo de calidad.

| # | Criterio | Atributo ISO 25010 | Evidencia |
|---|---|---|---|
| 1 | El cambio fue revisado y aprobado por al menos otra persona del equipo mediante Pull Request | Mantenibilidad (Analizabilidad) | PR con aprobación registrada en GitHub |
| 2 | Las pruebas unitarias automatizadas pasan y la cobertura de `src/` es ≥ 80 % | Mantenibilidad (Capacidad de ser probado) | Workflow de GitHub Actions en verde |
| 3 | Los criterios de aceptación de la historia fueron verificados por el Product Owner en el ambiente de pruebas | Adecuación funcional (Corrección funcional) | Comentario de aceptación del PO en la tarjeta |
| 4 | No hay vulnerabilidades altas/críticas en las dependencias ni secretos en el código | Seguridad (Confidencialidad) | Reporte de análisis (Dependabot / secret scanning) sin alertas abiertas |
| 5 | Existe un plan de reversión (rollback) probado y el despliegue está programado de lunes a jueves | Fiabilidad (Recuperabilidad) | Sección "Rollback" en el PR + fecha del despliegue |
| 6 | No quedan defectos abiertos de severidad crítica o alta asociados a la historia | Fiabilidad (Ausencia de fallos) | Tablero de defectos sin tarjetas críticas/altas ligadas a la historia |
