# Ejemplo de uso de API en forma genérica
# Del tutorial https://www.dataquest.io/blog/python-api-tutorial/
#%% Carga los modulos necesarios

import requests
import pandas as pd
from pprint import pprint

# Para más información de como funciona REST API
# https://www.restapitutorial.com

# Vamos a utilizar el API de OpenNotify de la NASA
# Más información en http://open-notify.org

#%% Vamos a obtener alguna información

# ¿Donde se encuentra en estos momentos la estación espacial?
response = requests.get("http://api.open-notify.org/iss-now.json")
pprint("\nStatus code: {}".format(response.status_code))
pprint("\nContenido: {}".format(response.content))

# Vamos a preguntar algo que no existe en la API
response = requests.get("http://api.open-notify.org/iss-pass")
print("\n\nStatus code: {}".format(response.status_code))
print("\nContenido: {}".format(response.content))

# Vamos a preguntar algo que si existe pero lo vamos apreguntar mal
response = requests.get("http://api.open-notify.org/iss-pass.json")
print("\n\nStatus code: {}".format(response.status_code))
print("\nContenido: {}".format(response.content))

#%% Realizar búsquedas con parámetros

# Revisando  http://open-notify.org/Open-Notify-API/ISS-Pass-Times/
# podemos ver que hay que dar lat y long (i.e. Hermosillo tiene 
# lat = 29.08919, lon = -110.96133)

#Vamos a ver cuando va a pasar la estacion espacial sobre nuesta cabeza

# Pasando los valores como parámetros
parametros = {
    "lat": 29.08919, 
    "lon": -110.96133
}
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parametros)
print("\n\nStatus code: {}".format(response.status_code))
print("\nContenido: {}".format(response.content))

# Pasando los parámetros dentro del cuerpo
response = requests.get("http://api.open-notify.org/iss-pass.json?lat=29.08919&lon=-110.96133")
print("\n\nStatus code: {}".format(response.status_code))
print("\nContenido: {}".format(response.content))


# %% Vamos a revisarlo como json
datos_dic = response.json()
pprint(datos_dic)

# %% Vamos a convertirlo en dataframe

datos_df = pd.DataFrame.from_dict(datos_dic['response'], orient="columns")
for (atr, valor) in datos_dic['request'].items():
    datos_df[atr] = valor
datos_df

# %%
