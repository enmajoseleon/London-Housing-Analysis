import pandas as pd
from sqlalchemy import create_engine
import openpyxl
df = pd.read_csv('london_houses.csv')
df.columns = df.columns.str.strip()

# --- FASE DE LIMPIEZA (Anti-Basura) ---
# 1. Filtro de realismo: Londres NO tiene mar. 
# Cambiamos "Sea" por "City View" o simplemente borramos esas filas sospechosas.
df = df[df['View'] != 'Sea']

# 2. Filtro de coherencia: Si quieres ser muy estricto, 
# podemos quedarnos solo con lo que no sea "basura" visual.
df = df.dropna() # Borra cualquier fila que tenga celdas vacías

# 3. Guardar en SQL (Sobreescribiendo la tabla anterior con datos limpios)
engine = create_engine('sqlite:///london_data.db')
df.to_sql('propiedades_limpias', con=engine, if_exists='replace', index=False)

print("✨ ¡Base de datos actualizada con datos LIMPIOS!")

# Ver el nuevo promedio sin la "basura" del mar
query = "SELECT Neighborhood, AVG([Price (£)]) as Promedio FROM propiedades_limpias GROUP BY Neighborhood ORDER BY Promedio DESC"
df_resultado = pd.read_sql(query, con=engine)
print(df_resultado)

# --- EXPORTACIÓN DE SEGURIDAD (EL PLAN MAESTRO) ---

# Exportamos a Excel (El estándar para reportes rápidos)
df.to_excel('datos_limpios_londres_final.xlsx', index=False)

# Exportamos a CSV (El "viejo confiable" que Power BI nunca rechaza)
df.to_csv('datos_limpios_londres_final.csv', index=False)

print("✅ ¡Archivos generados! Ahora sí, a brillar en Power BI.")