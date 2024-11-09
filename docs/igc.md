---
title: Ingeniería de características 
subtitle: Curso Ingeniería de Características
layout: page
hero_image: https://github.com/mcd-unison/ing-caract/raw/main/docs/img/transform-banner.jpg
hero_darken: true
show_sidebar: false
---

## Datos numéricos y cualitativos

1. [*Engineering Numeric Predictors*](http://www.feat.engineering/engineering-numeric-predictors.html)

2. [*Normalización y estandarización de datos numéricos*](https://towardsdatascience.com/clearly-explained-what-why-and-how-of-feature-scaling-normalization-standardization-e9207042d971)

3. [Algunas transformaciones en variables numéricas a considerar (`sci-kit learn` guide)](https://scikit-learn.org/stable/modules/preprocessing.html#non-linear-transformation)

4. [Un ejemplo en `sci-kit learn` de diferentes métodos de escalamiento](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_all_scaling.html#sphx-glr-auto-examples-preprocessing-plot-all-scaling-py)


5. [*All about Categorical Variable Encoding*](https://towardsdatascience.com/all-about-categorical-variable-encoding-305f3361fd02)

6. [*Encoding Categorical Predictors*](http://www.feat.engineering/encoding-categorical-predictors.html)

7. Biblioteca de python [`categorical_encoding`](https://github.com/alteryx/categorical_encoding) de Alteryx


8. [Libreta para colab con sklearn](https://colab.research.google.com/github/mcd-unison/ing-caract/blob/main/ejemplos/tipos/python/catnum.ipynb) y otra [libreta para colab con una librería especializada](https://github.com/mcd-unison/ing-caract/blob/main/ejemplos/tipos/python/categoricos.ipynb).

9. [*A Data Scientist’s Toolkit to Encode Categorical Variables to Numeric*](https://towardsdatascience.com/a-data-scientists-toolkit-to-encode-categorical-variables-to-numeric-d17ad9fae03f)

## Cadenas de caracteres

1. [Vectores de palabras](https://github.com/mcd-unison/ing-caract/raw/main/slides/vectores-palabras.pdf) 

2. Una [presentación con más detalle](https://github.com/mcd-unison/ing-caract/raw/main/slides/modelo-cbow.pdf)


## Variables georeferenciadas

1. [Una presentación muy agradable](https://kjordahl.net/SciPy-Tutorial-2015/#1) sobre el análisis de datos geoespaciales en python con herramientas libres.
   
2. Curso [Geographic Data Science](http://darribas.org/gds16/index.html) de [Dani Arribas-Bel](http://darribas.org). Tiene ejemplos en librets de python y presentaciones muy interesantes y accesibles.
   
3. [Material del curso de geoinformática](https://centrogeo.github.io/curso-geoinformatica-2/) del Laboratorio Nacional de Geointeligencia (GeoInt) de CentroGeo.

## Series de tiempo y variables de calendario

1. La documentación de `pandas`para fechas y horas [vuelta una libreta de jupyter](https://github.com/mcd-unison/ing-caract/blob/main/ejemplos/tipos/python/timestamp.ipynb)

2. [Un tutorial bastante completo en Kaggle de series de tiempo](https://www.kaggle.com/code/prashant111/complete-guide-on-time-series-analysis-in-python)

3. [Suavizado por medias móviles, filtro exponencial y *Holt-Winters*](https://medium.com/@srv96/smoothing-techniques-for-time-series-data-91cccfd008a2) y [Suavizado local](https://en.wikipedia.org/wiki/Local_regression) y en particular [LOESS](https://towardsdatascience.com/loess-373d43b03564)

4. [Un ejemplito sobre suavizado en python](https://colab.research.google.com/github/mcd-unison/ing-caract/blob/main/ejemplos/suavizado/suavizado.ipynb)


## Agregación

1. [Operadores de agregación](https://www.researchgate.net/profile/Magda-Komornikova/publication/285874074_Aggregation_operators_Properties_classes_and_construction_methods_Aggregation_operators_New_trends_and_applications/links/57832d7f08ae69ab88286d25/Aggregation-operators-Properties-classes-and-construction-methods-Aggregation-operators-New-trends-and-applications.pdf?_sg%5B0%5D=CnLFj_rNk1q8U3VLYbtDK1L94kNI1XBzFgrPK5vsO3b2vZYql03JSzRXon5rRZ2xnPUTo8w9lF96BTbSRhU3yA.B-4ecmBWT8oVAK6Y99nPSRyycwpAtU-ptO-jIj79Pod3oNsiVVnihUGgRhY1sEszKha86uC5gaq7tEr11gqjHw&_sg%5B1%5D=hKHosvszXiBud6dou0kAvJvHqDZ36T5UN6OYxiv6Cum8NMoqA4cdFvPPKezZbEy5viaF6O1nHHpBx5UW9Q2sQOlWZ_1mDC5COCf57riDQhhD.B-4ecmBWT8oVAK6Y99nPSRyycwpAtU-ptO-jIj79Pod3oNsiVVnihUGgRhY1sEszKha86uC5gaq7tEr11gqjHw&_iepl=), visto de un punto de vista muy formal. 
2. [Operadores de centro segun wikipedia](https://en.wikipedia.org/wiki/Average)
3. [Operadores de agregación OWA](https://www.researchgate.net/publication/228553904_OWA_Operators_in_Decision_Making).
4. Operadores del tipo [disyunción y conjunción](https://en.wikipedia.org/wiki/T-norm).
5. Agregación basada en [medidas de dispersión](https://en.wikipedia.org/wiki/Statistical_dispersion). 
6. Agregación en uno y múltiples indices [en R](https://dplyr.tidyverse.org/articles/grouping.html) y [en python](https://pandas.pydata.org/docs/getting_started/intro_tutorials/06_calculate_statistics.html).

## Selección de características

1. [*A Literature Review of Feature Selection Techniques and Applications*](https://github.com/mcd-unison/ing-caract/raw/main/pdf/feature-selection-review.pdf)
2. [*Permutation Importance*](https://scikit-learn.org/stable/modules/permutation_importance.html) en `sci-kit learn`.
3. [Selección de características](https://topepo.github.io/caret/feature-selection-overview.html) en `caret`.

## Generación de características

1. [Featuretools](https://www.featuretools.com). Herramienta para generación automática de atributos en función de la naturaleza de los atributos originales y una [libreta de ejemplo que me copié de la documentación](https://colab.research.google.com/github/mcd-unison/ing-caract/blob/main/ejemplos/featuretools/NHL_Games.ipynb).


![](https://imgs.xkcd.com/comics/machine_learning.png)


<!-- # Libros de consulta general

1. [R for Data Science](https://r4ds.had.co.nz), el libro de cabecera del *tidyverse*.

## ETL en todas partes

1. [Ploomber](https://docs.ploomber.io/en/latest/index.html) para establecer *pipelines* en Python.
   
2. Entrada de *Medium*: [How to Test Pandas ETL Data Pipeline](https://towardsdatascience.com/how-to-test-pandas-etl-data-pipeline-e49fb5dac4ce).

 -->
