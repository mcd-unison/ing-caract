# Carga los modulos necesarios

import xml.etree.ElementTree as et 
import os

pwd = '/Users/juliowaissman/Documents/cursos/IC-MCD-Unison/2021-2/ing-caract/ejemplos/integracion/python'
os.chdir(pwd)

# Abre en XML el archivo 

desayunos = et.parse("../ejemplos/ejemplo.xml")

for (i, des) in enumerate(desayunos.getroot()):
    print("Opción {}:".format(i))
    for prop in des:
        print("\t{}: {}".format(prop.tag, prop.text.strip()))

# Se puede buscar por etiquetas y subetiquetas

print("Los desayunos disponibles son: " + 
      ", ".join([p.text for p in desayunos.findall("food/name")]))
