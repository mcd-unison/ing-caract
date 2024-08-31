---
title: Análisis exploratorio de datos 
subtitle: Curso Ingeniería de Características
layout: page
hero_image: https://github.com/mcd-unison/ing-caract/raw/main/docs/img/eda-banner.jpg
hero_darken: true
show_sidebar: false 
---

## Tipos de datos

### Variables cualitativas

1. [Codificando variables categóricas en python](https://www.datacamp.com/community/tutorials/categorical-data), y [una muy breve libretita](https://colab.research.google.com/github/mcd-unison/ing-caract/blob/main/ejemplos/tipos/python/cat.ipynb).

### Fechas y horas

2. [¿Que es UTC?](https://en.wikipedia.org/wiki/Coordinated_Universal_Time) [¿Y el formato POSIX?](https://en.wikipedia.org/wiki/Unix_time).
3. [How To Manipulate Date And Time In Python Like A Boss](https://towardsdatascience.com/how-to-manipulate-date-and-time-in-python-like-a-boss-ddea677c6a4d)
3. [Working with datetime in Pandas DataFrame](https://towardsdatascience.com/working-with-datetime-in-pandas-dataframe-663f7af6c587)

### Manejo de cadenas de caracteres

1. [Procesamiento de texto](https://github.com/mcd-unison/ing-caract/raw/main/slides/tratamiento_texto.pdf) y su [libreta sobre expresiones regulares](https://github.com/mcd-unison/ing-caract/blob/main/ejemplos/tipos/python/regexp.ipynb) 
2. [Regex 101 (para armar expresiones regulares)](https://regex101.com)
3. [Regex tutorial — A quick cheatsheet by examples](https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285)
4. [Working with text data (pandas)](https://pandas.pydata.org/pandas-docs/stable/user_guide/text.html)
5. [NLP avanzado con SpaCy (curso)](https://course.spacy.io/en/)
6. Nubes de palabras [en python](https://amueller.github.io/word_cloud/) y [en R](https://cran.r-project.org/web/packages/wordcloud2/), y [una libreta con un ejemplo que hicimos para integrar `spacy` con `word_cloud`](https://github.com/mcd-unison/ing-caract/blob/main/ejemplos/tipos/python/nube_informe.ipynb)

### Series de tiempo

1. Un capitulo sobre una [Intoducción a las series de tiempo](http://www.ptolomeo.unam.mx:8080/xmlui/bitstream/handle/132.248.52.100/363/A5.pdf?sequence=5&isAllowed=y).
2. Libreta de colab [Working with Time Series](https://jakevdp.github.io/PythonDataScienceHandbook/03.11-working-with-time-series.html), como parte del libro en linea [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)

### Información georeferenciada 


1. [Geopandas](https://geopandas.org/en/stable/index.html#) 
2. Una [libreta de uso de geopandas](https://github.com/mcd-unison/ing-caract/blob/main/ejemplos/mapas/python/geopandas.ipynb) copiada directamente del [Material del curso de geoinformática](https://centrogeo.github.io/curso-geoinformatica-2/)
3. Archivos [geojson](https://geojson.org), [archivos Shape](https://en.wikipedia.org/wiki/Shapefile)
4. Para visualizar, lo más usado es la biblioteca [Leaflet](https://leafletjs.com) y su interface [para python](http://python-visualization.github.io/folium/).
5. Una [libreta para hacer mapas en python usando folium](https://github.com/mcd-unison/ing-caract/blob/main/ejemplos/mapas/python/Mapas-en-python.ipynb)


## Combinando tablas de datos

1. Combinación de dataframes [en python](https://pandas.pydata.org/docs/getting_started/intro_tutorials/08_combine_dataframes.html) 
2. Expansión en columnas o renglones [en python](https://pandas.pydata.org/docs/user_guide/reshaping.html)
3. Coeficientes de correlación de [Pearson](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient), [Spearman](https://en.wikipedia.org/wiki/Spearman%27s_rank_correlation_coefficient), [Kendall](https://en.wikipedia.org/wiki/Kendall_rank_correlation_coefficient) y[$\Phi_k$](https://phik.readthedocs.io/en/latest/index.html) (con [un ejemplito](https://github.com/KaveIO/PhiK/blob/master/phik/notebooks/phik_tutorial_basic.ipynb) de como usarla).


## Análisis exploratorio de datos

1. Motivación: [¿Porque las solas estadísticas descriptivas no son suficientes y un análisis exploratorio de datos siempre es necesario?](https://www.research.autodesk.com/publications/same-stats-different-graphs/)

1. [EDA ¿Qué es?](https://harvard-iacs.github.io/2018-CS109A/lectures/lecture-3/presentation/lecture3.pdf)
   
2. [Esta entrada de Medium con 5 herramientas de EDA automatizado](https://towardsdatascience.com/5-powerful-python-libraries-you-need-to-know-to-enhance-your-eda-process-f0100d563c16) y [esta otra, con algunas repetidas](https://pub.towardsai.net/5-python-packages-for-effortless-eda-94abddac3bc5) entre las que destacan:
      -  [YData profiling](https://docs.profiling.ydata.ai/),
      -  [D-Tale](https://github.com/man-group/dtale)
      -  [Sweetviz](https://github.com/fbdesignpro/sweetviz)
      -  [summarytools](https://github.com/6chaoran/jupyter-summarytools) 
      -  [AutoViz](https://github.com/AutoViML/AutoViz)
   

## Librerías para visualización de datos:

1. Exclusivas de python: [`matplotlib`](https://matplotlib.org/), [`seaborn`](https://seaborn.pydata.org/index.html) y [`holoviz`](https://holoviz.org)
2. General: [librerías abiertas de `plotly`](https://plotly.com/graphing-libraries/)

