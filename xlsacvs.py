import pandas as pd

def excel_to_csv(excel_file, csv_file):
    # Leer el archivo de Excel
    df = pd.read_excel(excel_file)

    # Escribir a CSV
    df.to_csv(csv_file, index=False)

# Uso del script
excel_file = 'Coordenadas.xlsx'
csv_file = 'Aulas.csv'
excel_to_csv(excel_file, csv_file)
