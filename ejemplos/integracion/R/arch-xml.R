#%% Archivos en xml
library("xml2")

#--------Leer archivo ejemplo xml-------------------
datos.xml <- read_xml("../ejemplos/ejemplo.xml")

for (des in xml_children(xml_root(datos.xml))){
  print("Opción:")
  for (atr in xml_children(des)){
    print(paste("   ", xml_name(atr), "->", xml_text(atr)))
  }
}


#-----Buscar por etiquetas y subetiquetas-----------
print("Las opciones disponibles son:")
for (menu in xml_find_all(datos.xml,"food/name")){
  print(xml_text(menu))
}
