---
title: Limpieza de Datos 
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
3. [Una opinión en contra de la discretización](https://medium.com/@peterflom/why-binning-continuous-data-is-almost-always-a-mistake-ad0b3a1d141f)
4. [Una opinión a favor de la discretización](https://towardsdatascience.com/sort-and-segment-your-data-into-bins-to-get-sorted-ranges-pandas-cut-and-qcut-7785931bbfde)

### Categóricos

1. [*All about Categorical Variable Encoding*](https://towardsdatascience.com/all-about-categorical-variable-encoding-305f3361fd02)
2. [*Encoding Categorical Predictors*](http://www.feat.engineering/encoding-categorical-predictors.html)
3. Biblioteca de python [`categorical_encoding](https://github.com/alteryx/categorical_encoding) de Alteryx
4. Paquete de R [`forcats`](https://forcats.tidyverse.org), parte del *tidyverse*
5. [Codificando variables categóricas en python](https://www.datacamp.com/community/tutorials/categorical-data)
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
7. Para practicar podemos usar las series te tiempo recuperadas de los informas estatales sobre la COVID19 por [Luís Armando Moreno Preciado](http://www.luisarmandomoreno.com)

### Manejo de cadenas de caracteres

1. [Procesamiento de texto](https://github.com/mcd-unison/ing-caract/raw/main/slides/tratamiento_texto.pdf)
2. [Regex 101 (para armar expresiones regulares)](https://regex101.com)
3. [Regex tutorial — A quick cheatsheet by examples](https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285)
4. [Working with text data (pandas)](https://pandas.pydata.org/pandas-docs/stable/user_guide/text.html)
5. [An Introduction to Text Processing and Analysis with R](https://m-clark.github.io/text-analysis-with-R/)
6. [NLP avanzado con SpaCy (curso)](https://course.spacy.io/en/)
7. Nubes de palabras [en python](https://amueller.github.io/word_cloud/) y [en R](https://cran.r-project.org/web/packages/wordcloud2/)

## Agregación

1. [Operadores de agregación](https://www.researchgate.net/profile/Magda-Komornikova/publication/285874074_Aggregation_operators_Properties_classes_and_construction_methods_Aggregation_operators_New_trends_and_applications/links/57832d7f08ae69ab88286d25/Aggregation-operators-Properties-classes-and-construction-methods-Aggregation-operators-New-trends-and-applications.pdf?_sg%5B0%5D=CnLFj_rNk1q8U3VLYbtDK1L94kNI1XBzFgrPK5vsO3b2vZYql03JSzRXon5rRZ2xnPUTo8w9lF96BTbSRhU3yA.B-4ecmBWT8oVAK6Y99nPSRyycwpAtU-ptO-jIj79Pod3oNsiVVnihUGgRhY1sEszKha86uC5gaq7tEr11gqjHw&_sg%5B1%5D=hKHosvszXiBud6dou0kAvJvHqDZ36T5UN6OYxiv6Cum8NMoqA4cdFvPPKezZbEy5viaF6O1nHHpBx5UW9Q2sQOlWZ_1mDC5COCf57riDQhhD.B-4ecmBWT8oVAK6Y99nPSRyycwpAtU-ptO-jIj79Pod3oNsiVVnihUGgRhY1sEszKha86uC5gaq7tEr11gqjHw&_iepl=), visto de un punto de vista muy formal. 
2. [Operadores de centro segun wikipedia](https://en.wikipedia.org/wiki/Average)
3. [Operadores de agregación OWA](https://www.researchgate.net/publication/228553904_OWA_Operators_in_Decision_Making).
4. Operadores del tipo [disyunción y conjunción](https://en.wikipedia.org/wiki/T-norm).
5. Agregación basada en [medidas de dispersión](https://en.wikipedia.org/wiki/Statistical_dispersion). 
6. Agregación en uno y múltiples indices [en R](https://dplyr.tidyverse.org/articles/grouping.html) y [en python](https://pandas.pydata.org/docs/getting_started/intro_tutorials/06_calculate_statistics.html).

## Operaciones comunes de limpieza en dataframes

1. Expansión en columnas o renglones [en python](https://pandas.pydata.org/docs/user_guide/reshaping.html) y [en R](https://tidyr.tidyverse.org/articles/pivot.html).
2. Combinación de dataframes [en python](https://pandas.pydata.org/docs/getting_started/intro_tutorials/08_combine_dataframes.html) y [en R](https://dplyr.tidyverse.org/articles/two-table.html). 

# Bibliotecas generales de limpieza de datos

1. [R for Data Science](https://r4ds.had.co.nz), el libro de cabecera del *tidyverse*.
2. [Data Cleaning in Python: the Ultimate Guide](https://towardsdatascience.com/data-cleaning-in-python-the-ultimate-guide-2020-c63b88bf0a0d). No es lo que el título trata vender pero si trae una guía de varias de las operaciones que normalmente hay que realizar para limpieza de datos.


