---
title: Contando historias con datos 
subtitle: Curso Ingeniería de Características
layout: page
hero_image: https://github.com/mcd-unison/ing-caract/raw/main/docs/img/redu-banner.jpg
hero_darken: true
show_sidebar: false
---


## Principios de visualización básicos

1. Libro [*Storytelling with data: a data visualization guide for business professionals*](https://www.storytellingwithdata.com)
de Cole Nussbaumer Knaflic, Wiley (2015), disponible en la librería de la DCEN.

2. Libro [Fundamentals of Data Visualization](https://clauswilke.com/dataviz/) de Claus O. Wilke. Buena introducción, con código en R.

3. Un muy bonito sitio [para escoger visualizaciones](https://datavizproject.com/#)

3. [Un checklist](https://github.com/mcd-unison/ing-caract/raw/main/pdf/DataVizChecklist.pdf) viejito pero útil para saber si mis gráficas son correctas.


## Tableros e indicadores clave de desempeño

1. [Sistemas de ayuda a la toma de decisiones](https://github.com/mcd-unison/ing-caract/raw/main/slides/dss.pptx)

2. Una [página de Qlik](https://www.qlik.com/us/kpi) sobre KPI's y [una guía](https://github.com/mcd-unison/ing-caract/raw/main/pdf/eb-kpi-planning-guide-en.pdf) para su desarrollo de la misma compañía.

3. [10 Best Practices for Building Effective Dashboards](https://github.com/mcd-unison/ing-caract/raw/main/pdf/BestPracticesDashboards.pdf) de Tableau


## Contando historias con datos

1. [Una revoltura de presentaciones](https://github.com/mcd-unison/ing-caract/raw/main/slides/storytelling1.pdf) con lo que más o menos saqué en claro de varios cursos de *DataCamp*
2. [¿Porqué contar historias?](https://github.com/mcd-unison/ing-caract/raw/main/slides/contando_historias.pdf) y algo sobre [conocer a tu audiencia](https://github.com/mcd-unison/ing-caract/raw/main/slides/audiencia.pdf), presentaciones de Joe Franklin para DataCamp.
3. [Un repositorio de github con un ejemplito mal hecho](https://github.com/juliowaissman/streamlit-mcd) qe se puede [consultar aquí](https://juliowaissman-mcd-ejemplito.streamlit.app). Lo vamos a usar de base para contar una historia.

![](https://imgs.xkcd.com/comics/self_description.png)

## Herramientas para desarrollar tablero

1. [Python tools for data visualization](https://pyviz.org) y también [un ejemplito en jupyter-flex](https://github.com/mcd-unison/ing-caract/raw/main/ejemplos/dashboards/jupyter-flex/dashboard-python.ipynb) y otro [ejemplito en panel](https://github.com/mcd-unison/ing-caract/raw/main/ejemplos/dashboards/panel/panel-demo.ipynb) 


3. [Streamlit](https://streamlit.io), una forma muy sencilla de hacer tableros en python. Revisar [la documentación](https://docs.streamlit.io), la sección de *get started* muy rápido nos enseña lo escencial.

4. [Dash open source](https://dash.plotly.com), la versión libre del *framework* de *Dash*. Una forma de crear tableros dinámicos complejos, pero que requiere una mayor complejidad en su programación, respecto a *Streamlit*.

5. [Streamlit vs Dash vs Voilà vs Panel — Battle of The Python Dashboarding Giants](https://medium.datadriveninvestor.com/streamlit-vs-dash-vs-voilà-vs-panel-battle-of-the-python-dashboarding-giants-177c40b9ea57#8026)

6. Para tableros dinámicos con filtros existen varias opciones comerciales que son importantes de conocer debido a que se uso se encuentra muy extendido en muchas empresas e instituciones:
   1. [PowerBI](https://powerbi.microsoft.com/es-mx/) de *Microsoft. Se puede acceder a *PowerBI* con la cuenta institucional, aunque solamente se tiene acceso a la versión limitada es suficiente para aprender a usarlo. Particularmente interesante es que se puede acceder a *PowerBI* desde *Teams* y tener visualizaciones para un equipo de trabajo.
   2. [Tableau](https://www.tableau.com) de *Salesforce*. Se pueden solicitar licencias sin costo y acceso a material de aprendizaje en los [programas académicos de Tableau](https://www.tableau.com/community/academic). Igualmente, se pueden hacer tableros y postearlos en forma pública con [Tableau Public](https://www.tableau.com/products/public).
   3. [Looker Studio](https://lookerstudio.google.com/overview) de *Google*. Es gratuito para usar desde la nube de Google con tu cuenta de *gmail* aunque la versión libre es relativamente simple.