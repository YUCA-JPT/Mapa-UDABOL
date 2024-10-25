import pandas as pd
import geojson
import re

# Función para convertir DMS a decimal
def dms_to_decimal(dms_str):
    parts = re.split('[°\'" ]+', dms_str)
    degrees = float(parts[0])
    minutes = float(parts[1])
    seconds = float(parts[2])
    direction = parts[3]
    decimal = degrees + minutes / 60 + seconds / 3600
    if direction in ['S', 'W']:
        decimal *= -1
    return decimal

# Leer el archivo CSV
csv_data = """Aulas,Latitud ,Longitud,DESCRIPCION
Cc1,"17° 23' 26.68"" S","66° 4' 7.79"" O",Ingenieria
Cc2,"17° 23' 26.48"" S","66° 4' 7.64"" O",Ingenieria
Cc2,"17° 23' 26.27"" S","66° 4' 7.56"" O",Ingenieria
Cc4,"17° 23' 26.08"" S","66° 4' 7.42"" O",Ingenieria/Arquitectura
C1,"17° 23' 25.17"" S","66° 4' 8.04"" O",Medicina
C2,"17° 23' 25.28"" S","66° 4' 7.81"" O",Medicina
C3,"17° 23' 25.44"" S","66° 4' 7.63"" O",Medicina
C4,"17° 23' 25.52"" S","66° 4' 7.45"" O",Medicina
D1,"17° 23' 25.97"" S","66° 4' 6.62"" O",Arquitectura
D2,"17° 23' 25.91"" S","66° 4' 6.91"" O",
D3,"17° 23' 25.80"" S","66° 4' 7.56"" O",
D4,"17° 23' 25.70"" S","66° 4' 8.26"" O",
D5,"17° 23' 25.64"" S","66° 4' 7.18"" O",
A 1,"17° 23' 26.85"" S","66° 4' 8.34"" O",MEDICINA
A 2,"17° 23' 27.01"" S","66° 4' 8.27"" O",
 A3,"17° 23' 27.69"" S","66° 4' 7.51"" O",
Chicas,"17° 23' 25.27"" S","66° 4' 6.77"" O",AREAS DE SANIDAD
Chicos,"17° 23' 25.30"" S","66° 4' 6.69"" O",AREAS DE SANIDAD
Piscina ,"17° 23' 25.66"" S","66° 4' 5.47"" O",AREAS DE COMVIVENCIA
Comedor,"17° 23' 25.78"" S","66° 4' 4.22"" O",AREAS DE COMVIVENCIA
Jefaturas,"17° 23' 25.90"" S","66° 4' 5.83"" O",Jefaturas
Biblioteca,"17° 23' 27.26"" S","66° 4' 6.37"" O",Biblioteca
Cajas-Ventanilla Unica,"17° 23' 27.12"" S","66° 4' 7.39"" O",Cajas-Ventanilla Unica
Cartera,"17° 23' 26.20"" S","66° 4' 6.00"" O",Cartera
Sala Audio Visual,"17° 23' 27.38"" S","66° 4' 7.34"" O",Sala Audio Visual
Fotocopiadora,"17° 23' 27.20"" S","66° 4' 7.55"" O",Fotocopiadora
Informacion y Marqueting,"17° 23' 26.96"" S","66° 4' 7.85"" O",Informacion y Marqueting
Apoyo Académico ,"17°39' 06.68"" S","66°06'84.16"" O",Apoyo Academico
Sala de Estudiantes,"17°39' 06.35 "" S","66°06'83.88"" O",Sala de Estudiantes
Cartera,"17°39' 06.20"" S","66°06'83.43"" O",Cartera
Aulas Docente,"17°39' 06.31"" S","66°06'83.37"" O",Aulas Docente
Aula T3,"17°39' 07.07"" S","66°06'83.41"" O",Aula T3
Laboratorio de Telecom,"17°39' 07.09"" S","66°06'83.33"" O",Laboratario de Telecom
Secretaria Regional,"17°39' 07.26"" S","66°06'83.52"" O",Secretaria Regional
Aula G-15,"17°39' 07.00"" S","66°06'83.57"" O",Aula G-15
Soporte Tecnico,,,Soporte Tecnico
Administracion de Redes,,,Administracion de Redes
Sala de Investigacion,"17°39' 06.81"" S","66°06' 83.40""O",Sala de Investigacion
Aula G-2,,,Aula G-2
Aula G-3,,,Aula G-3
Aula G-4,,,Aula G-4
Aula G-10,"17°39' 07.24"" S","66°06' 81.90"" O",Aula G-10
Aula G-5,"17°39' 07.37"" S","66°06' 83.59"" O",Aula G-5
Aula G-9,"17°39' 07.37"" S","66°06' 83.59"" O",Aula G-9
Aula G-7,"17°39' 07.09"" S","66°06' 84.29"" O",Aula G-7
Aula G-6,"17°39' 07.09"" S","66°06' 84.29"" O",Aula G-6
Baños Administrativo ,"17°39' 07.09"" S","66°06' 84.29""O",Baño Administrador
Aula G-12,"17°39' 05.74"" S","66°06' 82.75"" O",Aula G-12
Vicerrector,,,Vicerrector
Aula G-16,"17°39' 06.49"" S","66°06' 83.02""O",Aula G-16
Aula G-19,"17°39' 06.93"" S","66°06' 83.28""O",Aula G-19
Aula G-18,"17°39' 07.30"" S","66°06' 83.50""O",Aula G-18
Aula G-17,"17°39' 07.30"" S","66°06' 83.50""O",Aula G-17
"""

df = pd.read_csv(pd.compat.StringIO(csv_data))

# Crear la lista de características GeoJSON
features = []
for _, row in df.iterrows():
    if pd.notnull(row['Latitud ']) and pd.notnull(row['Longitud']):
        lat = dms_to_decimal(row['Latitud '])
        lon = dms_to_decimal(row['Longitud'])
        point = geojson.Point((lon, lat))
        feature = geojson.Feature(geometry=point, properties={
            "Aula": row['Aulas'],
            "Descripcion": row['DESCRIPCION']
        })
        features.append(feature)

# Crear el objeto GeoJSON
feature_collection = geojson.FeatureCollection(features)

# Guardar el GeoJSON en un archivo
with open('output.geojson', 'w') as f:
    geojson.dump(feature_collection, f)
