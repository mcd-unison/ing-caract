---
title: Integración de Datos 
subtitle: Curso Ingeniería de Características
layout: page
hero_image: https://github.com/mcd-unison/ing-caract/raw/main/docs/img/download-banner.jpg
hero_darken: true
show_sidebar: false
---

## Integración de datos

1. [Ingeniería de datos 101](https://github.com/mcd-unison/ing-caract/raw/main/slides/data-eng-101.pdf)
2. Una presentación (medio propagandistica, pero buena) de [*DeltaLake*](https://github.com/mcd-unison/ing-caract/raw/main/slides/deltalake.pdf)
- [DataBricks, community edition](https://www.databricks.com/try-databricks)
- [Para solicitar acceso a los cursos de DataBricks](https://docs.google.com/forms/d/1xa7NHz5mWh5y40KiyshOi4_XJRnWIVGrtyqI0uNvyFE/edit) y un [archivo con instrucciones para ingresar a los Cursos](https://github.com/mcd-unison/ing-caract/raw/main/pdf/databricks-instructions.pdf)


## Tipos de archivos, y como leerlos en python y R

1. Archivos CSV
2. Archivos [JSON](https://www.json.org/json-en.html)
3. Archivos [XML](https://www.w3schools.com/xml/default.asp)
4. Archivos [HDF](https://asdc.larc.nasa.gov/documents/tools/hdf.pdf)
5. Archivos [Excel](https://www.linkedin.com/pulse/why-all-data-scientists-learn-ms-excel-karthik-shashidhar)
6. Archivos [Parquet](https://databricks.com/glossary/what-is-parquet)


## En donde encontrar datos

1. El [INEGI](https://www.inegi.org.mx/default.html)
2. Plataforma [DataMéxico](https://datamexico.org/es) y su [interesante API](https://dev-api.datamexico.org/ui/)
3. El portal de [datos abiertos del gobierno de México](https://datos.gob.mx)
4. Micrositio de [incidencia delictiva](https://www.gob.mx/sesnsp/acciones-y-programas/incidencia-delictiva-299891?state=published) del secretariado ejecutivo nacional, [CONEVAL](https://www.coneval.org.mx/Paginas/principal.aspx), [CONAPO](https://www.gob.mx/conapo)
5. El portal de [Datamx](http://datamx.io) o el de [Data Civica](https://datacivica.org)
6. [Explorador de datos delictivos de México](http://www.morlan.mx/explorador_delictivo/) desarrollado por Morlan.
7. [7 portales de datos abiertos](https://github.com/mcd-unison/ing-caract/raw/main/pdf/fuentelibreinfo.JPG). Gracias, Malena, por compartirlo.
8. [Kaggle](https://www.kaggle.com/datasets)
9. El [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php) (para los viejitos)
10. [Google Dataset Search](https://datasetsearch.research.google.com)
11. [Listado de algunas APIs abiertas](https://github.com/public-apis/public-apis) y otro [de APIs gratuitas](https://free-apis.github.io)

## Descargando archivos

### Con comandos de UNIX

- [Un bonito acordeón de `curl`](https://curl.se/docs/manual.html)
- Libro gratuito [Data Science at the Command Line, 2e](https://www.datascienceatthecommandline.com/2e/)

### Usando R

- Usando [`ddownload.file`](https://www.rdocumentation.org/packages/utils/versions/3.6.2/topics/download.file)
- Descargando los datos [Directamente cuando se leen](https://www.datacamp.com/community/tutorials/r-data-import-tutorial?utm_source=adwords_ppc&utm_campaignid=1658343524&utm_adgroupid=63833881815&utm_device=c&utm_keyword=%2Bread%20%2Bdata%20%2Br&utm_matchtype=b&utm_network=g&utm_adpostion=&utm_creative=469789579419&utm_targetid=aud-522010995285:kwd-309793905111&utm_loc_interest_ms=&utm_loc_physical_ms=1010167&gclid=CjwKCAjw092IBhAwEiwAxR1lRvFJfvVx6UVJMwqkAUiVf7v6mqs-m5V2Ti3umTn1qbwYYvQOisnMRxoC2RgQAvD_BwE).
- [Acordeón de R para descarga de archivos](https://raw.githubusercontent.com/rstudio/cheatsheets/main/data-import.pdf)
- [Usando la API desde R](https://github.com/mcd-unison/ing-caract/raw/main/slides/ReadingFromAPIs.pdf)
- [Webscraping con R](https://github.com/mcd-unison/ing-caract/raw/main/slides/ReadingFromTheWeb.pdf)
- [Ejemplito de RMarkdown para descarga de datos](https://github.com/mcd-unison/ing-caract/raw/main/ejemplos/integracion/R/descarga_datos.Rmd)

### Usando python

- [Descargando archivos con las librerías estándar](https://betterprogramming.pub/3-simple-ways-to-download-files-with-python-569cb91acae6)
- [Descargando datos con Pandas](https://towardsdatascience.com/direct-to-pandas-dataframe-ab2e97ae7574)
- [Acordeón de python para descarga de datos](http://datacamp-community-prod.s3.amazonaws.com/72e88aa1-b4f2-4658-9d86-15becf8263df)
- [Tutorial para el uso de Rest API en python](https://realpython.com/api-integration-in-python/), y [este otro](https://towardsdatascience.com/quick-fire-guide-to-apis-in-python-891dd98c8877)
- [Tutorial de Beautiful Soup 4](https://beautiful-soup-4.readthedocs.io)
- [Una libreta de ejemplito](https://github.com/mcd-unison/ing-caract/blob/main/ejemplos/integracion/python/descarga_datos.ipynb) y [otra con el uso de una API mal documentada](https://github.com/mcd-unison/ing-caract/blob/main/ejemplos/integracion/python/RNPDNO-API.ipynb)

### SQL

- Curso [SQL for Data Analysis](https://www.udacity.com/course/sql-for-data-analysis--ud198) de Udacity



