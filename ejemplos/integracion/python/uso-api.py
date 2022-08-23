# Ejemplo de uso de API en forma genérica

import requests
import pandas as pd
from pprint import pprint

# Para más información de como funciona REST API
# https://www.restapitutorial.com

# ¿Que queremos encontrar en una API abierta?
pregunta = "https://dev-api.datamexico.org/tesseract/cubes/anuies_status/aggregate.jsonrecords?drilldowns%5B%5D=Geography+Municipality.Geography.State&measures%5B%5D=Students&parents=false&sparse=false"
response = requests.get(pregunta)
print("STATUS")
print(response.status_code)

print("\n\nCONTENIDO\n\n")
print(response.content)
