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
3. Limpieza de datos, la cual debe incluir:
   1. Armonización de variables.
   2. Manejo correcto y codificación de datos cuantitativos, cualitativos, fechas y horas.
   3. Manejo de valores perdidos.
   4. Detección y manejo de valores anómalos.
4. Análisis exploratorio de datos, que utilice:
   1. Métodos de agregación.
   2. Suavizado para series de tiempo o manejo de datos georeferenciados.
   3. Al menos un método de reducción de características (PCA, t-SNE,...).
5. Generación de un conjunto de datos arreglados (*tidy data*), para lo que es necesario:
   1. Un script (R o python) de limpieza básica que lea los datos crudos y devuelva los datos acomodados.
   2. Los datos en forma *tidy*, ya sea en *csv*, *parquet*, o *SQlite*.
   3. Un diccionario de datos especificando las descripciones de cada atributo y sus unidades
6. Visualización de los datos. 

Recuerda que este proceso es iterativo, y que muchas veces el EDA determina nuevas formas de realizar el tratamiento de datos, pero al final será necesario contar con las siguientes evidencias:

1. Repositorio de github con su página respectiva que se defina y explique el proyecto. Todas las evidencias siguientes se encontrarán dentro del repositorio (y la página respectiva).
2. Script(s) o programa(s) de adquisición de datos y limpieza.
3. Datos en formato *tidy* y su diccionario de datos correspondiente.
4. Reporte de EDA (ya sea en tablero, libreta y tipo reporte).
5. Tablero de visualización de los datos que cuenten una historia e incluyan métodos de agregación y uso de al menos un método de reducción de dimensionalidad.