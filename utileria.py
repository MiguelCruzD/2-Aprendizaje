"""
Este archivo contiene funciones que se utilizan en el miniproyecto.

Como leer archivos de datos y formatearlos para que sean utilizados en los algoritmos.
"""

from urllib3 import request
import urllib.request
import zipfile

def descarga_datos(url, archivo):
    """
    Descarga un archivo de datos de una URL.
    
    Parámetros
    ----------
    url : str
        URL de donde se descargará el archivo.
    archivo : str
        Nombre del archivo donde se guardará la descarga.
    """
    urllib.request.urlretrieve(url, archivo)
    return None

def descomprime_zip(archivo, directorio='datos'):
    """
    Descomprime un archivo zip.
    
    Parámetros
    ----------
    archivo : str
        Nombre del archivo zip.
    directorio : str
        Directorio donde se descomprimirá el archivo.
    """
    with zipfile.ZipFile(archivo, 'r') as zip_ref:
        zip_ref.extractall(directorio)
    return None

def lee_csv(archivo, atributos=None, separador=',', tiene_encabezado=False):
    with open(archivo, 'r') as f:
        lineas = f.readlines()

    if atributos is None and tiene_encabezado:   
        columnas = lineas[0].strip().split(separador)
        lineas = lineas[1:]  # Omitimos la primera línea
    else:
        columnas = atributos

    datos = []
    for l in lineas:
        valores = l.strip().split(separador)
        print(valores)  # 👈 Verifica qué valores tiene cada línea
        datos.append({c: v for c, v in zip(columnas, valores)})

    print(datos[:5])  # Muestra los primeros datos para verificar
    return datos

