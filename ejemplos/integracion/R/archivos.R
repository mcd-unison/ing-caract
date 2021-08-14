# Descargando y abriendo archivos


# 1. setwd() y getwd()
# 2. Archivos con dirección relativa y absoluta
getwd()
setwd("/Users/juliowaissman/Documents/cursos/IC-MCD-Unison/2021-2/ing-caract/ejemplos/integracion/R")
getwd()

# En R es por convención usar . como parte 
# de los nombres de variables y funciones
if (!dir.exists("../data/")){
  dir.create("../data")
}

# Vamos a ver como le hacemos con archivos excel

covid.url <- "http://datosabiertos.salud.gob.mx/gobmx/salud/datos_abiertos/datos_abiertos_covid19.zip"
covid.archivo <- "../data/datos_abiertos_covid19.zip"
covid.dic.conceptos.url <- "http://epidemiologia.salud.gob.mx/gobmx/salud/datos_abiertos/diccionario_datos_covid19.zip"
covid.dic.conceptos.archivo <- "../data/diccionario.zip"

# ¿No suena parecido? Hagamos una función
if(!file.exists(covid.archivo)){
  download.file(covid.url, destfile = covid.archivo)  
  unzip(covid.archivo, exdir = "../data/")
  download.file(covid.dic.conceptos.url, destfile = covid.dic.conceptos.archivo)  
  unzip(covid.dic.conceptos.archivo, exdir = "../data/")
  fecha.descarga <- date()
}

info <- data.frame(
  concepto = c('Fecha de descarga', 'URL', 'Archivo', 'Diccionario URL', 'Diccionario'),
  valor = c(fecha.descarga, covid.url, covid.archivo, covid.dic.conceptos.url, covid.dic.conceptos.archivo)
)
write.csv(x = info, file = "../data/info.txt")
