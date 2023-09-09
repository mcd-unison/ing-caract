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

1. Un archivo `README.md` que expñlique cual sería el objetivo final del análisis (aunque fuera en forma muy genética) y que justifique las acciones que se van a tomar (cuales  fuentes se usan, cuales variables se retienen, el tipo de limpieza de los datos, las tablas *tidy* seleccionadas,...).

1. Un script o libreta que descargue datos de al menos dos fuentes diferentes, y que genere un archivo texto con la descripción de las fuentes, las fechas de descarga y de ser posible la descripción (o enlaces) que expliquen la naturaleza de los datos descargados. Si los datos venían sin explicación, agregar la explicación propia para simplificar el proceso.
   
2. Una libreta o script que transforme y utilice los datos de acuerdo a su tipo, selecciones la información que se desea utilizar y se generen los *Dataframes* necesarios.
   
3. Un diccionario de datos por cada *dataframe*

Como extra se considerará la implementación de algún método para asegurar la calidad de los datos.

Todo esto deberá estar en un repositorio de *Github* en el cual se desarrolle el trabajo. Yo les recomiendo que creen una organización, en la cual participen todos los miembros del equipo en un repositorio público.

La entrega del trabajo será que cada miembro del equipo suba en la plataforma Teams, de manera individual el enlace al repositorio.


## Posibles proyectos

### Semáforo delictivo

Se tiene el siguiente sitio: http://www.semaforo.com.mx/ 

Donde se propone un semáforo delictivo, al cual se le pueden ver claramente varios problemas para que represente claramente a un semaforo delictivo en forma general. 

La idea final es proponer diferentes KPIs así como un tablero interactivo que pueda *sustituir* al semáforo. Para realizarlo se necesitará integrar *al menos* dos bases de datos:

- Censo poblacional del INEGI (para calcular tasas delictivas por cada 100,000 hab.), o proyecciones de población de la CONAPO.

- Datos de incidencia delictiva publicado por el secretariado ejecutivo: https://www.gob.mx/sesnsp/acciones-y-programas/datos-abiertos-de-incidencia-delictiva 

*Usuario:* **Estephanía Pivac Alcaráz** 

Subdirectora de Datos Abiertos. Subsecretaría de Gobierno Digital del Estado de Sonora.

### ¿Cómo la producción agropecuaria y/o pesquera se relaciona con trabajos generados?

Exste es un proyecto de interés de la SAGARPA en el que solicitan la colaboración de la Subsecretaría de Gobierno Digital del Estado de Sonora. 

Aquí se integrarían varias fuentes de datos:

- Datos de SAGARHPA: https://sagarhpa.sonora.gob.mx/
  
- Agricultura: https://datos.sonora.gob.mx/conjuntos-de-datos/mostrar/datos-de-agricultura-sonora/1573
  
- Ganadería: https://datos.sonora.gob.mx/conjuntos-de-datos/mostrar/datos-ganaderia-sonora/1581
  
- Pesca: https://datos.sonora.gob.mx/conjuntos-de-datos/mostrar/datos-pesca-sonora/1582
Información del IMSS: http://datos.imss.gob.mx/dataset/asg2023/resource/asg-2023-01-31

- IMSS: http://datos.imss.gob.mx/dataset/asg2023/resource/asg-2023-01-31

*Usuario:* **Estephanía Pivac Alcaráz** 

Subdirectora de Datos Abiertos. Subsecretaría de Gobierno Digital del Estado de Sonora.


### ¿Es posible preever excedentes agricolas?

Los excedentes agrícolas son una de las vías en que la Red de Bancos de Alimentos de México (RedBAMX) obtiene insumos, los cuales distribuye a una población que sufre de inseguridad alimentaria. Poder prever un excedente agrícola puede permitir a la RedBAMX buscar aliados entre los productores como parte del proyecto estratégico [pacto por la comida](https://pactoporlacomida.org).

Se busca iniciar con una exploración de los datos siguientes:

- Sistema SIAP: https://www.gob.mx/siap

- Precios del Mercado Agricola: http://www.economia-sniim.gob.mx/nuevo/Home.aspx?opcion=Consultas/MercadosNacionales/PreciosDeMercado/Agricolas/ConsultaFrutasYHortalizas.aspx?SubOpcion=4|0

- Información de la Secretaría de Economía (DataMexico)

*Usuario:* **Everardo Riestra Ochoa** 

Coordinador Nacional de Alianzas Agrícolas Transfronterizas de la RedBAMX.


### Indicadores delictivos

Hay varias suposiciones sobre la precedencia de delitos en el estado de Sonora. ¿La violencia intrafamiliar precede al homicidio doloso? ¿El robo de vehículos tiene relación con delitos mayores? ¿Hay relación con condiciones socioeconómicas respecto a ciertos tipos de delitos? Tratar de responder estas preguntas. Este proyecto está fuertemente ligado con el proyecto del semaforo delictivo, por lo que posiblemente los fusionemos en un solo trabajo.


*Usuario:* **Victor Manuel Ibarra Encinas**

Fiscalía del Estado de Sonora


