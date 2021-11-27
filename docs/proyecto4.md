---
title: Proyecto 4. Un proceso de ingeniería de características
subtitle: Curso Ingeniería de Características
layout: page
hero_image: https://github.com/mcd-unison/ing-caract/raw/main/docs/img/iintegrabanner.png
hero_darken: true
show_sidebar: false
---

Como proyecto final vamos a tener un proceso simple pero completo de ingeniería de características. El proyecto debe constar con las siguientes fases:

1. Una descripción del problema que se busca resolver (la parte del modelado o la presentación del producto final no nos interesa por el momento pero se debe tener claras las intenciones para las cuales se realiza la ingeniería de características)
2. Obtención de la información usando al menos dos fuentes diferentes. Recopilación de la información cruda (*raw data*) en forma reproducible.
3. Un análisis exploratorio de datos sencillo (EDA)
4. Generación de un conjunto de datos arreglados (*tidy data*), para lo que es necesario:
   1. Un script (R o python) de limpieza básica que lea los datos crudos y devuelva los datos acomodados
   2. Los datos en forma *tidy*, ya sea en *csv*, *parquet*, o *SQlite*
   3. Un diccionario de datos especificando las descripciones de cada atributo y sus unidades
5. Limpieza de datos, la cual debe incluir:
   1. Armonización de variables
   2. Manejo correcto y codificación de datos cuantitativos, cualitativos, fechas y horas.
   3. Manejo de valores perdidos
   4. Detección y manejo de valores anómalos (*outliers*)
6. Visualización de la información utilizando un método de reducción de características (PCA, t-SNE,...)

La limpieza de datos puede estar integrada en el script para generar los datos *tidy* o puede hacerse posteriormente, dependiendo el problema.

El EDA también puede hacerse al inicio o al final.

El problema debe ser simple, pero ilustrativo. Mientras más complejo es el problema a resolver el proceso de ingeniería de características es más tedioso y largo. Es un proyecto integrador que ilustre el uso de las técnicas. 
