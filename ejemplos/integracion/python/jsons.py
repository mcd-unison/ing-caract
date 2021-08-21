#%% Cargar librerias
import os  # Para manejo de archivos y directorios
import urllib # Una forma estandard de descargar datos
import pandas as pd
import json # Una forma estandar de leer archivos json 

# %% Abrir archivos Json con pandas
archivo_url = "https://api.github.com/users/juliowaissman/repos"
archivo_nombre = "../data/repos.json"

pwd = '/Users/juliowaissman/Documents/cursos/IC-MCD-Unison/2021-2/ing-caract/ejemplos/integracion/python'
os.chdir(pwd)
if not os.path.exists(archivo_nombre):
    urllib.request.urlretrieve(archivo_url, archivo_nombre)

# Como cargarlos y como verlos
df_repos = pd.read_json(archivo_nombre)
#df_repos.owner.apply(lambda x: x['login'])

#%% Abrir archivos json usando la librería json
with open(archivo_nombre, 'r') as fp:
    repos = json.load(fp)

print("\nNúmero de entradas: {}".format(len(repos)))
print("\nNombre de los atributos: {}".format(", ".join(repos[0].keys())))
print("\nAtributos de 'owner': {}".format(", ".join(repos[0]['owner'].keys())))
