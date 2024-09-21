---
title: Proyecto 1. Descargando datos de la web
subtitle: Curso Ingeniería de Características
layout: page
hero_image: https://github.com/mcd-unison/ing-caract/raw/main/docs/img/API-banner.jpg
hero_darken: true
show_sidebar: false
---


## Selección de un problema

Para el resto del curso vamos a trabajar sobre el mismo problema, basado en datos reales públicos, los cuales van a tener que descargar. Para esta primera etapa, cada equipo deberá hacer lo siguiente:

1. Seleccionar un tema o una problemática, y especificar cual es la pregunta que se piensa contestar al final de los 3 proyectos del curso. Para que la problemática sea válida deberá implicar el uso de los siguientes tipos de datos:
   1. Que implique alguna base de datos con series de tiempo.
   2. Que maneje información georeferenciada (como estados, municipios, AGEBs, ...)
   3. Que incluya datos cualitativos y cuantitativos.
   4. Si hay datos que vienen en forma de texto (aunque se puedan tratar) es una característica deseable pero no obligatoria.
   5. Que use al menos dos fuentes de datos.

2. Indicar cual es el público a el que está destinado el producto de datos final (tablero).

3. Indicar en una lista las fuentes primarias de datos donde se encuentra la información.

4. Generar una asociación en *GitHub* e inicializar un proyecto con [cookiecutter data science](https://cookiecutter-data-science.drivendata.org), y especificar en el archivo `README.md` toda la información de los 3 incisos anteriores.

## Obtención y limpieza de datos

La obtención de datos es muy importante, y fuera de los datos públicos que podemos descargar directamente como archivos `csv`, `json` o `xml`, es importante saber como utilizar una API para poder obtener datos de diferentes aplicaciones. Igualmente, es importante saber como tratar cada tipo de datos que tenemos y tener una visión general de ellos.

En este proyecto, cada equipo va a desarrollar un pequeño programa que ayude a descargar datos a partir de diferentes APIs, o usando un método para descargas masivas. Recuerda de usar un entorno virtual, y dejar especificado el método de descarga de datos en el archivo `makefile`. 

Las evidencias para esta etapa del proyecto será:

1. Un script que descargue datos de al menos dos fuentes diferentes, y que genere un archivo texto con la descripción de las fuentes, las fechas de descarga y de ser posible la descripción (o enlaces) que expliquen la naturaleza de los datos descargados. Si los datos venían sin explicación, agregar la explicación propia para simplificar el proceso. Los datos se deberán guardar en `.data/raw/`. Pueden hacer primero una libreta para probar cosas (en la sección de `notebooks`)

2. Una libreta o script que transforme y utilice los datos `raw` de acuerdo a su tipo, seleccione la información que se desea utilizar y se generen los conjuntos de datos *tidy* necesarios. Estos conjuntos se deben de guardad en `./data/processed/` o si hay pasos intermedios en `./data/interim`. Pueden hacer primero una libreta para probar cosas (en la sección de `notebooks`) 

3. Un diccionario de datos por cada conjunto de datos, los diccionarios de datos deben de ir en `./references/` y deben estar claramente indicados.

4. Algún método para asegurar la calidad de los datos. Solo las reglas de calidad más sencillas u obvias.

5. Agregar al archivo `README.md` la explicación de como inicializar el entorno virtual, de como ejecutar la descarga de los datos, así como ejecutar el procesamiento inicial a tablas de datos *tidy*.

## Comunicación

Uno de los miembros del equipo va a hacer una entrada de *Medium*

