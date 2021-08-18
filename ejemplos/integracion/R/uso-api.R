# Para más información de como funciona REST API
# https://www.restapitutorial.com

# Vamos a utilizar el API de OpenNotify de la NASA
# Más información en http://open-notify.org

#----------Vamos a obtener alguna información-----------------

# ¿Donde se encuentra en estos momentos la estación espacial?
response <- httr::GET("http://api.open-notify.org/iss-now.json")
print(paste("Status:", response$status_code))
print(paste("Contenido:", httr::content(response, as = 'text')))

# Vamos a preguntar algo que no existe en la API
response <- httr::GET("http://api.open-notify.org/iss-pass")
print(paste("Status:", response$status_code))
print(paste("Contenido:", httr::content(response, as = 'text')))

# Vamos a preguntar algo que si existe pero lo vamos apreguntar mal
response <- httr::GET("http://api.open-notify.org/iss-pass.json")
print(paste("Status:", response$status_code))
print(paste("Contenido:", httr::content(response, as = 'text')))

#-----------Vamos a leer con parametros----------------------

parametros = list(
  lat = 29.08919, 
  lon = -110.96133
)
response <- httr::GET("http://api.open-notify.org/iss-pass.json", query = parametros)
print(paste("Status:", response$status_code))
contenido <- httr::content(response, as = 'parsed')
