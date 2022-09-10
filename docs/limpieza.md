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
5. [Una opinión en contra de la discretización](https://medium.com/@peterflom/why-binning-continuous-data-is-almost-always-a-mistake-ad0b3a1d141f)
6. [Una opinión a favor de la discretización](https://towardsdatascience.com/sort-and-segment-your-data-into-bins-to-get-sorted-ranges-pandas-cut-and-qcut-7785931bbfde)

### Categóricos

1. [*All about Categorical Variable Encoding*](https://towardsdatascience.com/all-about-categorical-variable-encoding-305f3361fd02)
2. [*Encoding Categorical Predictors*](http://www.feat.engineering/encoding-categorical-predictors.html)
3. Biblioteca de python [`categorical_encoding`](https://github.com/alteryx/categorical_encoding) de Alteryx
4. Paquete de R [`forcats`](https://forcats.tidyverse.org), parte del *tidyverse*
5. [Codificando variables categóricas en python](https://www.datacamp.com/community/tutorials/categorical-data), con una [libreta para colab](https://github.com/mcd-unison/ing-caract/blob/main/ejemplos/tipos/python/categoricos.ipynb).
6. [*A Data Scientist’s Toolkit to Encode Categorical Variables to Numeric*](https://towardsdatascience.com/a-data-scientists-toolkit-to-encode-categorical-variables-to-numeric-d17ad9fae03f)
7. [*Factors (R for DataScience)*](https://r4ds.had.co.nz/factors.html)
8. [*A guide to encoding categorical features using R*](https://www.r-bloggers.com/2020/02/a-guide-to-encoding-categorical-features-using-r/)
9. [*Encode Smarter: How to Easily Integrate Categorical Encoding into Your Machine Learning Pipeline*](https://innovation.alteryx.com/encode-smarter/)


### Fechas y horas

1. [¿Que es UTC?](https://en.wikipedia.org/wiki/Coordinated_Universal_Time) [¿Y el formato POSIX?](https://en.wikipedia.org/wiki/Unix_time).
2. [How To Manipulate Date And Time In Python Like A Boss](https://towardsdatascience.com/how-to-manipulate-date-and-time-in-python-like-a-boss-ddea677c6a4d)
3. [Working with datetime in Pandas DataFrame](https://towardsdatascience.com/working-with-datetime-in-pandas-dataframe-663f7af6c587)
4. [It’s merely a matter of time, Dr. Watson! Understanding date and time in R](https://towardsdatascience.com/its-merely-a-matter-of-time-dr-watson-2fd74a648842)
5. [*5 most practically useful operations when-working with date and time in R*](https://blog.exploratory.io/5-most-practically-useful-operations-when-working-with-date-and-time-in-r-9f9eb8a17465)
6. El paquete [`lubridate`](https://lubridate.tidyverse.org) como parte del *tidyverse*.
7. Para ver como funciona `lubridate` vamos a descargar [el *Rmarkdown* del vignette de lubridate (oficial)](https://github.com/tidyverse/lubridate/raw/0bb49b21c88736240219dc67e7ed0eb3df15d9b1/vignettes/lubridate.Rmd "download")
8. La documentación de `pandas`para fechas y horas [vuelta una libreta de jupyter](https://github.com/mcd-unison/ing-caract/blob/main/ejemplos/tipos/python/timestamp.ipynb)

### Manejo de cadenas de caracteres

1. [Regex 101 (para armar expresiones regulares)](https://regex101.com)
2. [Regex tutorial — A quick cheatsheet by examples](https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285)
3. [Procesamiento de texto](https://github.com/mcd-unison/ing-caract/raw/main/slides/tratamiento_texto.pdf) y su [libreta sobre expresiones regulares](https://github.com/mcd-unison/ing-caract/blob/main/ejemplos/tipos/python/texto.ipynb) 
4. [Working with text data (pandas)](https://pandas.pydata.org/pandas-docs/stable/user_guide/text.html)
5. [An Introduction to Text Processing and Analysis with R](https://m-clark.github.io/text-analysis-with-R/)
6. [NLP avanzado con SpaCy (curso)](https://course.spacy.io/en/)
7. Nubes de palabras [en python](https://amueller.github.io/word_cloud/) y [en R](https://cran.r-project.org/web/packages/wordcloud2/)


### Actividades de aprendizaje

1. Realizar los ejercicios de esta [libreta sobre tipos numéricos](https://github.com/mcd-unison/ing-caract/blob/main/ejemplos/tipos/python/numericos.ipynb)
2. Desarrollar un archivo *RMarkdown* sobre codificación de variables cualitativas que exporte a formato `pdf`o `html` (o inclusive en modo presentación) y que explique e incluta código que ejemplifique:
   1. El método *One hot encoding*
   2. Un método de contraste (*Helmert*, *Backward difference*, *polinomial*)
   3. Un método de codificación bayesiano (*Target*, +Leave one out*, *WoE*, *Stein*, *M*)
   4. Puedes basarte en [este tutorial](https://www.r-bloggers.com/2020/02/a-guide-to-encoding-categorical-features-using-r/) que trae su [propio código](https://github.com/radmuzom/categorical_encoding). Esto último es opcional.
3. Realizar el *Coursera project network* de [expresiones regulares en python](https://www.coursera.org/programs/universidad-de-sonora-on-coursera-ggm7m/data-science/all-data-science?productId=kVjg-qnzEeuLCQ6P36XDuw&productType=course&showMiniModal=true&source=browse)
4. Realizar el curso de [Data wrangling](https://enterprise.edx.org/uni-sonora/course/HarvardX+PH125.6x) de Harvard que se encuentra en EdX.