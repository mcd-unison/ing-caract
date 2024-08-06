---
title: Proyecto 1. Descargando datos de la web
subtitle: Curso Ingeniería de Características
layout: page
hero_image: https://github.com/mcd-unison/ing-caract/raw/main/docs/img/API-banner.jpg
hero_darken: true
show_sidebar: false
---


## Obtención y limpieza de datos

La obtención de datos es muy importante, y fuera de los datos públicos que podemos descargar directamente como archivos `csv`, `json` o `xml`, es importante saber como utilizar una API para poder obtener datos de diferentes aplicaciones. Igualmente, es importante saber como tratar cada tipo de datos que tenemos y tener una visión general de ellos.

En este proyecto, cada equipo va a desarrollar un pequeño programa que ayude a descargar datos a partir de diferentes APIs, o usando un método para descargas masivas. 

Los requisitos para este proyecto deberán estar presentes en un repositorio de GitHub público con las siguientes características:

1. Un archivo `README.md` que explique cual sería el objetivo final del análisis (aunque fuera en forma muy genética) y que justifique las acciones que se van a tomar (cuales  fuentes se usan, cuales variables se retienen, el tipo de limpieza de los datos, las tablas *tidy* seleccionadas,...).

1. Un script o libreta que descargue datos de al menos dos fuentes diferentes, y que genere un archivo texto con la descripción de las fuentes, las fechas de descarga y de ser posible la descripción (o enlaces) que expliquen la naturaleza de los datos descargados. Si los datos venían sin explicación, agregar la explicación propia para simplificar el proceso.
   
2. Una libreta o script que transforme y utilice los datos de acuerdo a su tipo, selecciones la información que se desea utilizar y se generen los *Dataframes* necesarios.
   
3. Un diccionario de datos por cada *dataframe*

Como extra se considerará la implementación de algún método para asegurar la calidad de los datos.

Todo esto deberá estar en un repositorio de *Github* en el cual se desarrolle el trabajo. Yo les recomiendo que creen una organización, en la cual participen todos los miembros del equipo en un repositorio público.

La entrega del trabajo será que cada miembro del equipo suba en la plataforma Teams, de manera individual el enlace al repositorio.


## Posibles proyectos

### Semáforo delictivo

Se tiene el siguiente [semáforo delictivo propuesto](http://www.semaforo.com.mx/),
donde se propone un semáforo delictivo, al cual se le pueden ver claramente varios problemas.

La idea final es proponer diferentes KPIs así como un tablero interactivo que pueda *sustituir* al semáforo. Para realizarlo se necesitará integrar *al menos* dos bases de datos:

- Censo poblacional del [INEGI](https://www.inegi.org.mx/datosabiertos/) (para calcular tasas delictivas por cada 100,000 hab.), o proyecciones de población de la [CONAPO](https://www.gob.mx/conapo/documentos/bases-de-datos-de-la-conciliacion-demografica-1950-a-2019-y-proyecciones-de-la-poblacion-de-mexico-2020-a-2070?idiom=es).

- [Datos de incidencia delictiva publicado por el secretariado ejecutivo](https://www.gob.mx/sesnsp/acciones-y-programas/datos-abiertos-de-incidencia-delictiva).


*Usuario:* **Diana Ballesteros** 

Directora de inteligencia de datos. Subsecretaría de Gobierno Digital del Estado de Sonora.

### ¿Cómo la producción agropecuaria y/o pesquera se relaciona con trabajos generados?

Exste es un proyecto de interés de la SAGARPA en el que solicitan la colaboración de la Subsecretaría de Gobierno Digital del Estado de Sonora. 

Aquí se integrarían varias fuentes de datos:

- [Datos de SAGARHPA](https://sagarhpa.sonora.gob.mx/).
  
- [Agricultura](https://datos.sonora.gob.mx/conjuntos-de-datos/mostrar/datos-de-agricultura-sonora/1573).
  
- [Ganadería](https://datos.sonora.gob.mx/conjuntos-de-datos/mostrar/datos-ganaderia-sonora/1581).
  
- [Pesca](https://datos.sonora.gob.mx/conjuntos-de-datos/mostrar/datos-pesca-sonora/1582).
  
- [Información del IMSS](http://datos.imss.gob.mx/dataset/asg2023/resource/asg-2023-01-31).


*Usuario:* **Diana Ballesteros** 

Directora de inteligencia de datos. Subsecretaría de Gobierno Digital del Estado de Sonora.


### ¿Es posible predecir excedentes agrícolas?

Los excedentes agrícolas son una de las vías en que la Red de Bancos de Alimentos de México (RedBAMX) obtiene insumos, los cuales distribuye a una población que sufre de inseguridad alimentaria. Poder prever un excedente agrícola puede permitir a la RedBAMX buscar aliados entre los productores como parte del proyecto estratégico [pacto por la comida](https://pactoporlacomida.org).

Se busca iniciar con una exploración de los datos siguientes:

- [Sistema SIAP](https://www.gob.mx/siap).

- [Precios del Mercado Agricola](http://www.economia-sniim.gob.mx/nuevo/).

- Información de la Secretaría de Economía ([DataMexico](https://www.economia.gob.mx/datamexico/))

y aquí se presenta un ejemplo de un [tablero](https://amhpac.org/negociosymercados/socios/v2/produccion/) de la AMHPAC.

*Usuario:* **Everardo Riestra Ochoa** 

Coordinador Nacional de Alianzas Agrícolas Transfronterizas de la RedBAMX.


### ¿Que pasa con los migrantes cuando pasan por Sonora?

Los migrantes cuando pasan por el estado de Sonora pasan por muchos peligro. Entre los peligros más importantes que están ocurriendo actualmente es el secuestro de migrantes indocumentados. A partir de los datos publicos tanto de la *US Customs and Border Protection (CBP)* del gobierno de EEUU, como de la información abierta de incidencia delictiva del secretariado ejecutvo, se busca hacer un estudio a nivel estatal como de los municipios fronterizos para identificar relaciones de delitos asociados con los migrantes. Un mejor entendimiento de los peligros que corren los migrantes es necesario para desarrollar mejores estrategias para su protección.

Se busca armonizar los datos del CBP con los del secretariado ejecutivo y completar la información, para poder contar una historia sobre algunos de los peligros que enfrentan los migrantes en su paso por Sonora. Se piensa utilizar las bases de datos abiertas siguientes:

- [Datos de incidencia delictiva publicado por el secretariado ejecutivo](https://www.gob.mx/sesnsp/acciones-y-programas/datos-abiertos-de-incidencia-delictiva) 

- [US Customs and Border Protection Data Portal](https://www.cbp.gov/newsroom/stats/cbp-public-data-portal)


*Usuario:* **Victor Manuel Ibarra Encinas**

Director general de análisis estratégico y política criminal. Fiscalía del Estado de Sonora


