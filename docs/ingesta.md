---
title: Ingesta de datos 
subtitle: Curso Ingeniería de Características
layout: page
hero_image: https://github.com/mcd-unison/ing-caract/raw/main/docs/img/download-banner.jpg
hero_darken: true
show_sidebar: false
---


## Tipos de archivos, y como leerlos en python

1. Archivos CSV
2. Archivos [JSON](https://www.json.org/json-en.html)
3. Archivos [XML](https://www.w3schools.com/xml/default.asp)
4. Archivos [HDF](https://asdc.larc.nasa.gov/documents/tools/hdf.pdf)
5. Archivos [Excel](https://www.linkedin.com/pulse/why-all-data-scientists-learn-ms-excel-karthik-shashidhar)
6. Archivos [Parquet](https://databricks.com/glossary/what-is-parquet)

## Descargando archivos

### Con comandos de UNIX

- [Un bonito acordeón de `curl`](https://curl.se/docs/manual.html)
- Libro gratuito [Data Science at the Command Line, 2e](https://www.datascienceatthecommandline.com/2e/)


<!-- ### Usando R

- Usando [`ddownload.file`](https://www.rdocumentation.org/packages/utils/versions/3.6.2/topics/download.file)
- Descargando los datos [Directamente cuando se leen](https://www.datacamp.com/community/tutorials/r-data-import-tutorial?utm_source=adwords_ppc&utm_campaignid=1658343524&utm_adgroupid=63833881815&utm_device=c&utm_keyword=%2Bread%20%2Bdata%20%2Br&utm_matchtype=b&utm_network=g&utm_adpostion=&utm_creative=469789579419&utm_targetid=aud-522010995285:kwd-309793905111&utm_loc_interest_ms=&utm_loc_physical_ms=1010167&gclid=CjwKCAjw092IBhAwEiwAxR1lRvFJfvVx6UVJMwqkAUiVf7v6mqs-m5V2Ti3umTn1qbwYYvQOisnMRxoC2RgQAvD_BwE).
- [Acordeón de R para descarga de archivos](https://raw.githubusercontent.com/rstudio/cheatsheets/main/data-import.pdf)
- [Usando la API desde R](https://github.com/mcd-unison/ing-caract/raw/main/slides/ReadingFromAPIs.pdf)
- [Webscraping con R](https://github.com/mcd-unison/ing-caract/raw/main/slides/ReadingFromTheWeb.pdf)
- [Ejemplito de RMarkdown para descarga de datos](https://github.com/mcd-unison/ing-caract/raw/main/ejemplos/integracion/R/descarga_datos.Rmd)
 -->
### Usando python

- [Documentación de Pandas para entrada y salida](https://pandas.pydata.org/docs/user_guide/io.html)
- [Tutorial para el uso de Rest API en python](https://realpython.com/api-integration-in-python/)
- [Una libreta con el uso de una API mal documentada](https://colab.research.google.com/github/mcd-unison/ing-caract/blob/main/ejemplos/integracion/python/RNPDNO-API.ipynb)
- [Una libreta de ejemplo](https://colab.research.google.com/github/mcd-unison/ing-caract/blob/main/ejemplos/integracion/python/descarga_datos.ipynb)
- [Tutorial de Beautiful Soup 4](https://beautiful-soup-4.readthedocs.io)
- [Librería para descargar archivos públicos desde el *Google Drive* en forma programática](https://github.com/wkentaro/gdown) (Gracias a Estephanía por compartirlo con todos)

### SQL

- Curso [SQL for Data Analysis](https://www.udacity.com/course/sql-for-data-analysis--ud198) de Udacity


## En donde encontrar datos sobre México

1. El [INEGI](https://www.inegi.org.mx/default.html) y una [herramienta de consulta en python](https://github.com/FabioSol/INEGIExplorer)
2. Plataforma [DataMéxico](https://www.economia.gob.mx/datamexico/) y su [interesante API](https://www.economia.gob.mx/datamexico/es/vizbuilder)
3. El portal de [datos abiertos del gobierno de México](https://datos.gob.mx)
4. El portel de [datos abiertos del gobierno de Sonora](https://datos.sonora.gob.mx)
5. [Incidencia delictiva](https://www.gob.mx/sesnsp/acciones-y-programas/incidencia-delictiva-299891?state=published) del secretariado ejecutivo nacional y un ejemplo de un [explorador de datos delictivos de México](http://www.morlan.mx/explorador_delictivo/) desarrollado por Morlan.
6. [CONEVAL](https://www.coneval.org.mx/Paginas/principal.aspx) y [CONAPO](https://www.gob.mx/conapo)
7. El portal de [Datamx](http://datamx.io)
8. [*Our World in Data*](https://ourworldindata.org) y su [repositorio base en GitHub](https://github.com/owid)
9. [7 portales de datos abiertos](https://github.com/mcd-unison/ing-caract/raw/main/pdf/fuentelibreinfo.JPG). Gracias, Malena, por compartirlo.
10. [Kaggle](https://www.kaggle.com/datasets)
11. El [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php) (para los viejitos)
12. [Google Dataset Search](https://datasetsearch.research.google.com)
13. [Listado de algunas APIs abiertas](https://github.com/public-apis/public-apis) y otro [de APIs gratuitas](https://free-apis.github.io)



## Calidad de datos

### Aseguramiento de la calidad de los datos

1. Una [presentación sobre calidad de los datos](https://github.com/mcd-unison/ing-caract/raw/main/slides/calidad_dato.pdf).
2. [Pydantic](https://docs.pydantic.dev/latest/), una librería para validar y serializar datos en Python; y su versión para datos en `DataFrames`de pandas, [Pandantic](https://pandantic-rtd.readthedocs.io/en/latest/).
3. [Pandera](https://www.union.ai/pandera), una librería basada en evaluar directamente los *DataFrames*, con una [documentación](https://pandera.readthedocs.io/en/stable/index.html#) bastante completa.
4. [Great Expectations](https://greatexpectations.io), una librería en python para asegurar la calidad de los datos. Y [una libreta con un sobrevuelo rápido para su uso](https://colab.research.google.com/github/mcd-unison/ing-caract/blob/main/ejemplos/calidad/great_expectations_intro.ipynb).

### Auditabilidad de los datos

1. [DVC](https://dvc.org) o *Data Version Control*, [una presentacioncita](https://github.com/mcd-unison/ing-caract/raw/main/slides/dvc.pdf) y [un ejemplito de la documentación](https://dvc.org/doc/start?tab=Mac-Linux)
2. [Deltalake](https://delta.io), el [libro de O'Relly sobre Deltalake](https://delta.io/pdfs/DLDTG_ER5.pdf), y un [acordeón para SQL y para python](https://delta.io/pdfs/DLDTG_ER5.pdf)
3. [Hopsworks](https://www.hopsworks.ai), otro *Lakehouse* como *Deltalake*, versión sin costo y empresarial, siempre en la nube.

![](https://www.explainxkcd.com/wiki/images/d/d7/flawed_data.png)
