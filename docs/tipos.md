---
title: Tipos de Datos 
subtitle: Curso Ingeniería de Características
layout: page
hero_image: https://github.com/mcd-unison/ing-caract/raw/main/docs/img/organize-banner.jpg
hero_darken: true
show_sidebar: false
---

## Representación y acondicionamiento por tipo de datos

### Numéricos 

1. [*Engineering Numeric Predictors*](http://www.feat.engineering/engineering-numeric-predictors.html)

2. [*Normalización y estandarización de datos numéricos*](https://towardsdatascience.com/clearly-explained-what-why-and-how-of-feature-scaling-normalization-standardization-e9207042d971)

3. [Algunas transformaciones en variables numéricas a considerar (`sci-kit learn` guide)](https://scikit-learn.org/stable/modules/preprocessing.html#non-linear-transformation)

4. [Un ejemplo en `sci-kit learn` de diferentes métodos de escalamiento](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_all_scaling.html#sphx-glr-auto-examples-preprocessing-plot-all-scaling-py)

### Categóricos

1. [*All about Categorical Variable Encoding*](https://towardsdatascience.com/all-about-categorical-variable-encoding-305f3361fd02)

2. [*Encoding Categorical Predictors*](http://www.feat.engineering/encoding-categorical-predictors.html)

3. Biblioteca de python [`categorical_encoding`](https://github.com/alteryx/categorical_encoding) de Alteryx


4. [Codificando variables categóricas en python](https://www.datacamp.com/community/tutorials/categorical-data), con una [libreta para colab con sklearn](https://github.com/mcd-unison/ing-caract/blob/main/ejemplos/tipos/python/catnum.ipynb) y otra [libreta para colab con una librería especializada](https://github.com/mcd-unison/ing-caract/blob/main/ejemplos/tipos/python/categoricos.ipynb).

5. [*A Data Scientist’s Toolkit to Encode Categorical Variables to Numeric*](https://towardsdatascience.com/a-data-scientists-toolkit-to-encode-categorical-variables-to-numeric-d17ad9fae03f)


### Fechas y horas

1. [¿Que es UTC?](https://en.wikipedia.org/wiki/Coordinated_Universal_Time) [¿Y el formato POSIX?](https://en.wikipedia.org/wiki/Unix_time).
2. [How To Manipulate Date And Time In Python Like A Boss](https://towardsdatascience.com/how-to-manipulate-date-and-time-in-python-like-a-boss-ddea677c6a4d)
3. [Working with datetime in Pandas DataFrame](https://towardsdatascience.com/working-with-datetime-in-pandas-dataframe-663f7af6c587)
4. La documentación de `pandas`para fechas y horas [vuelta una libreta de jupyter](https://github.com/mcd-unison/ing-caract/blob/main/ejemplos/tipos/python/timestamp.ipynb)

### Manejo de cadenas de caracteres

1. [Procesamiento de texto](https://github.com/mcd-unison/ing-caract/raw/main/slides/tratamiento_texto.pdf) y su [libreta sobre expresiones regulares](https://github.com/mcd-unison/ing-caract/blob/main/ejemplos/tipos/python/regexp.ipynb) 
2. [Regex 101 (para armar expresiones regulares)](https://regex101.com)
3. [Regex tutorial — A quick cheatsheet by examples](https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285)
4. [Working with text data (pandas)](https://pandas.pydata.org/pandas-docs/stable/user_guide/text.html)
5. [NLP avanzado con SpaCy (curso)](https://course.spacy.io/en/)
6. Nubes de palabras [en python](https://amueller.github.io/word_cloud/) y [en R](https://cran.r-project.org/web/packages/wordcloud2/), y [una libreta con un ejemplo que hicimos para integrar `spacy` con `word_cloud`](https://github.com/mcd-unison/ing-caract/blob/main/ejemplos/tipos/python/nube_informe.ipynb)
7. [Vectores de palabras](https://github.com/mcd-unison/ing-caract/raw/main/slides/vectores-palabras.pdf) y una [presentación con más detalle](https://github.com/mcd-unison/ing-caract/raw/main/slides/modelo-cbow.pdf)

## Series de tiempo

1. Un capitulo sobre una [Intoducción a las series de tiempo](http://www.ptolomeo.unam.mx:8080/xmlui/bitstream/handle/132.248.52.100/363/A5.pdf?sequence=5&isAllowed=y).
2. Libreta de colab [Working with Time Series](https://jakevdp.github.io/PythonDataScienceHandbook/03.11-working-with-time-series.html), como parte del libro en linea [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)
3. [Suavizado por medias móviles, filtro exponencial y *Holt-Winters*](https://medium.com/@srv96/smoothing-techniques-for-time-series-data-91cccfd008a2) y [Suavizado local](https://en.wikipedia.org/wiki/Local_regression) y en particular [LOESS](https://towardsdatascience.com/loess-373d43b03564)
5. [Un tutorial bastante completo en Kaggle](https://www.kaggle.com/code/prashant111/complete-guide-on-time-series-analysis-in-python)
6. [Un ejemplito sobre suavizado en python](https://colab.research.google.com/github/mcd-unison/ing-caract/blob/main/ejemplos/suavizado/suavizado.ipynb)

## Información georeferenciada (mapas)

1. [Una presentación muy agradable](https://kjordahl.net/SciPy-Tutorial-2015/#1) sobre el análisis de datos geoespaciales en python con herramientas libres.
2. Curso [Geographic Data Science](http://darribas.org/gds16/index.html) de [Dani Arribas-Bel](http://darribas.org). Tiene ejemplos en librets de python y presentaciones muy interesantes y accesibles.
3. [Material del curso de geoinformática](https://centrogeo.github.io/curso-geoinformatica-2/) del Laboratorio Nacional de Geointeligencia (GeoInt) de CentroGeo.
4. [Geopandas](https://geopandas.org/en/stable/index.html#) 
5. Para visualizar, lo más usado es la biblioteca [Leaflet](https://leafletjs.com) y su interface [para python](http://python-visualization.github.io/folium/).
6. Archivos [geojson](https://geojson.org), [archivos Shape](https://en.wikipedia.org/wiki/Shapefile)

## Como hacer mapas

1. Una [presentación realizada por Luís Armando Moreno](https://github.com/mcd-unison/ing-caract/raw/main/slides/Mapas%20coropléticos.pdf), con su respectivo [ejemplo ilustrativo](https://github.com/mcd-unison/ing-caract/raw/main/ejemplos/mapas/R/GMU-Ejemplo.R).
2. Una [libreta de uso de geopandas](https://github.com/mcd-unison/ing-caract/blob/main/ejemplos/mapas/python/geopandas.ipynb) copiada directamente del [Material del curso de geoinformática](https://centrogeo.github.io/curso-geoinformatica-2/)
3. Una [libreta para hacer mapas en python usando folium](https://github.com/mcd-unison/ing-caract/blob/main/ejemplos/mapas/python/Mapas-en-python.ipynb)
