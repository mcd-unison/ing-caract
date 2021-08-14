# Archivos json

library(jsonlite)

if (!dir.exists("../data/")){
  dir.create("../data")
}

# Descargar archivo (una sola vez)
archivo.url <- "https://api.github.com/users/juliowaissman/repos"
archivo.nombre <- "../data/repos.json"
if(!file.exists(archivo.nombre)){
  download.file(archivo.url, destfile = archivo.nombre, method = "curl")  
  fecha.descarga <- date()
}

r.json <- fromJSON(archivo.nombre)

