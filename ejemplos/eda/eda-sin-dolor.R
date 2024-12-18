# Priero vamos a bajar dos bases de juguete de Kaggle:
#    https://www.kaggle.com/mirichoi0218/insurance/
#    https://www.kaggle.com/c/titanic
#
# Como te piden que estés registrado y aceptes términos de kaggle,
# pues la tendremos que bajar a pie.


#--------- Primer opción (sencilla pero carismática) ----------------

# Aqui va tu propio directorio o lo puedes hacer a pie
# Este comando solo usalo una sola vez, y verifica el directorio
setwd(paste(getwd(), 'ejemplos', 'eda', sep='/'))
dir(getwd())

library(readr)
url_insurance <- "https://github.com/mcd-unison/ing-caract/raw/main/ejemplos/eda/insurance.csv"
url_titanic <- "https://github.com/mcd-unison/ing-caract/raw/main/ejemplos/eda/titanic.csv"

df <- read_csv(url_insurance)

#---------- Usando explore(mas acá) ---------------------------------

library(explore)
explore(df)

#--------- Tercera opción (la más perrona) ---------------------------

library('dataMaid')

makeDataReport(df,
               render = FALSE,
               file = "insurance_dataMaid.Rmd",
               replace = TRUE)


