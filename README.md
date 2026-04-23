# London Housing Analysis 🏠🇬🇧

## Descripción
Procesamiento de datos inmobiliarios de Londres usando **Python** para la limpieza y **Power BI** para la visualización geoespacial. El proyecto se enfoca en resolver desafíos comunes de ingeniería de datos, como la falta de identificadores únicos y errores de agregación en métricas de precio.

## 🛠️ Tecnologías utilizadas
* **Python (Pandas):** Limpieza de datos y pre-procesamiento.
* **Power BI:** Modelado de datos y creación de dashboards interactivos.
* **DAX:** Creación de medidas personalizadas para análisis de promedios.

## 🚀 Desafíos Resueltos
* **Integridad de Datos:** La fuente original carecía de IDs únicos, lo que causaba errores de agrupación. Se implementó una columna de índice para forzar el contexto de fila.
* **Corrección de Métricas:** Se detectaron anomalías en el cálculo de promedios globales. Se resolvió mediante columnas calculadas y medidas DAX (`AVERAGE`) para asegurar que el precio por m² fuera exacto por barrio.
* **Geolocalización:** Optimización de campos de ubicación para representación precisa en mapas.

## 📊 Visualización
El dashboard permite comparar el costo de vida entre zonas como **Chelsea** y **Greenwich**, revelando disparidades económicas significativas en el mercado londinense.
