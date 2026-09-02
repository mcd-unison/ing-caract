---
title: Análisis exploratorio de datos 
subtitle: Curso Ingeniería de Características
layout: page
hero_image: https://github.com/mcd-unison/ing-caract/raw/main/docs/img/eda-banner.jpg
hero_darken: true
show_sidebar: false 
---


## Agregación de la información

1. Combinación de dataframes [en python](https://pandas.pydata.org/docs/getting_started/intro_tutorials/08_combine_dataframes.html) 
2. Expansión en columnas o renglones [en python](https://pandas.pydata.org/docs/user_guide/reshaping.html)

3. Coeficientes de correlación de [Pearson](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient), [Spearman](https://en.wikipedia.org/wiki/Spearman%27s_rank_correlation_coefficient), [Kendall](https://en.wikipedia.org/wiki/Kendall_rank_correlation_coefficient) y [$\Phi_k$](https://phik.readthedocs.io/en/latest/index.html) (con [un ejemplito](https://github.com/KaveIO/PhiK/blob/master/phik/notebooks/phik_tutorial_basic.ipynb) de como usarla).

4. [Una plantilla para definir KPIs](https://bernardmarr.com/a-sample-kpi-template/) que me parece bastante clara. No es la única y puedes escoger la que se ajuste a tus necesidades. 


## Análisis exploratorio de datos

1. Motivación: [¿Porque las solas estadísticas descriptivas no son suficientes y un análisis exploratorio de datos siempre es necesario?](https://www.research.autodesk.com/publications/same-stats-different-graphs/)

2. Hay que tener cuidado, correlación no significa causalidad como lo muestran estas [*spurious correlations*](https://www.tylervigen.com/spurious-correlations). 

![](https://imgs.xkcd.com/comics/heatmap.png)

3. [EDA ¿Qué es?](https://harvard-iacs.github.io/2018-CS109A/lectures/lecture-3/presentation/lecture3.pdf)
   
4. [Esta entrada de Medium con 5 herramientas de EDA automatizado](https://towardsdatascience.com/5-powerful-python-libraries-you-need-to-know-to-enhance-your-eda-process-f0100d563c16) y [esta otra, con algunas repetidas](https://pub.towardsai.net/5-python-packages-for-effortless-eda-94abddac3bc5) entre las que destacan:
      -  [YData profiling](https://docs.profiling.ydata.ai/),
      -  [D-Tale](https://github.com/man-group/dtale)
      -  [Sweetviz](https://github.com/fbdesignpro/sweetviz)
      -  [summarytools](https://github.com/6chaoran/jupyter-summa rytools) 
      -  [AutoViz](https://github.com/AutoViML/AutoViz)
5. [Un ejemplito del uso de los AutoEDAs](https://colab.research.google.com/github/mcd-unison/ing-caract/blob/main/ejemplos/eda/auto-eda.ipynb)
   

## Librerías para visualización de datos:

1. Exclusivas de python: [`matplotlib`](https://matplotlib.org/), [`seaborn`](https://seaborn.pydata.org/index.html) y [`holoviz`](https://holoviz.org)
2. General: [librerías abiertas de `plotly`](https://plotly.com/graphing-libraries/)
3. Tableros sencillos con filtros: [*Streamlit*](https://streamlit.io) y [*Panel*](https://panel.holoviz.org/index.html)

