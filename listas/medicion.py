import pandas as pd

def agregar_registro():
    fecha = input("Ingrese la fecha (AAAA-MM-DD): ")
    hora = input("Ingrese la hora (HH:MM:SS): ")
    medicion = float(input("Ingrese la medición en kW: "))
    # ... (agregar campos para fotografía y notas)

    registro = {
        'fecha': fecha,
        'hora': hora,
        'medicion': medicion,
        # ...
    }

    # Agregar el registro a una lista o DataFrame
    datos.append(registro)

# Crear una lista para almacenar los registros
datos = []

# Ejemplo de uso:
agregar_registro()
agregar_registro()

# Convertir los datos a un DataFrame para facilitar el análisis
df = pd.DataFrame(datos)

# Calcular el consumo diario (ejemplo simplificado)
df['consumo_diario'] = df['medicion'].diff()

# Guardar los datos en un archivo CSV
df.to_csv('consumo.csv', index=False)
