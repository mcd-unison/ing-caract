# Carga archivos desde internet (muchas formas de hacerlo)

import os  # Para manejo de archivos y directorios
import urllib.request # Una forma estandard de descargar datos
# import requests # Otra forma no de las librerías de uso comun

import datetime # Fecha de descarga
import pandas as pd # Solo para ver el archivo descargado
import zipfile # Descompresión de archivos



# pwd
print(os.getcwd())

#  Ahora vamos a bajar los datos de COVID y leer un archivo excel
covid_url = "http://datosabiertos.salud.gob.mx/gobmx/salud/datos_abiertos/datos_abiertos_covid19.zip"
covid_archivo = "../data/datos_abiertos_covid19.zip"
covid_dic_conceptos_url = "http://datosabiertos.salud.gob.mx/gobmx/salud/datos_abiertos/diccionario_datos_covid19.zip"
covid_dic_conceptos_archivo = "../data/diccionario.zip"

if not os.path.exists(covid_archivo):
    urllib.request.urlretrieve(covid_url, covid_archivo)  
    with zipfile.ZipFile(covid_archivo, "r") as zip_ref:
        zip_ref.extractall("../data/")
    
    urllib.request.urlretrieve(covid_dic_conceptos_url, covid_dic_conceptos_archivo)  
    with zipfile.ZipFile(covid_dic_conceptos_archivo, "r") as zip_ref:
        zip_ref.extractall("../data/")

    with open("../data/info.txt", 'w') as f:
        f.write("Archivos Covid Mexico\n")
        f.write("Descargado el " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        f.write("Desde: " + covid_url + "\n")
        f.write("Nombre: " + covid_archivo + "\n")
        f.write("Diccionario de datos desde: " + covid_dic_conceptos_url + "\n")
        f.write("Nombre: " + covid_dic_conceptos_archivo + "\n")
    