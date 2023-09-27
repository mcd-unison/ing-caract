---
title: Análisis exploratorio de datos 
subtitle: Curso Ingeniería de Características
layout: page
hero_image: https://github.com/mcd-unison/ing-caract/raw/main/docs/img/eda-banner.jpg
hero_darken: true
show_sidebar: false 
---

## Análisis exploratorio de datos

1. [EDA ¿Qué es?](https://github.com/mcd-unison/ing-caract/raw/main/slides/exploratoryGraphs.pdf)
   
2. Python: [Pandas profiling](https://github.com/pandas-profiling/pandas-profiling), [otras herramientas](https://medium.com/spatial-data-science/4-tools-to-speed-up-exploratory-data-analysis-eda-in-python-e240ebcd18de). Un [script](https://github.com/mcd-unison/ing-caract/raw/main/ejemplos/eda/p-profile-en-script.py) para usar el el curso y generar un reporte EDA automatizado.
   
3. R: [`dlookr`](https://cran.r-project.org/web/packages/dlookr/vignettes/EDA.html), [SmartEDA](https://github.com/daya6489/SmartEDA), capítulo del libro [R for Data Science](https://r4ds.had.co.nz/exploratory-data-analysis.html), y muchos más. Un [script en R](https://github.com/mcd-unison/ing-caract/raw/main/ejemplos/eda/eda-sin-dolor.R) para probar con la generación de EDA automatizados.

4. Coeficientes de correlación de [Pearson](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient), [Spearman](https://en.wikipedia.org/wiki/Spearman%27s_rank_correlation_coefficient), [Kendall](https://en.wikipedia.org/wiki/Kendall_rank_correlation_coefficient) y[$\Phi_k$](https://phik.readthedocs.io/en/latest/index.html) (con [un ejemplito](https://github.com/KaveIO/PhiK/blob/master/phik/notebooks/phik_tutorial_basic.ipynb) de como usarla).

## Librerías para visualización de datos:

1. Python: [`matplotlib`](https://matplotlib.org/), [`seaborn`](https://seaborn.pydata.org/index.html) y [`holoviz`](https://holoviz.org)
2. R: [`ggplot2`](https://ggplot2.tidyverse.org/) y sus [`extensiones`](https://exts.ggplot2.tidyverse.org/gallery/)
3. General: [librerías abiertas de `plotly`](https://plotly.com/graphing-libraries/)

## Selección de características

1. [*A Literature Review of Feature Selection Techniques and Applications*](https://github.com/mcd-unison/ing-caract/raw/main/pdf/feature-selection-review.pdf)
2. [*Permutation Importance*](https://scikit-learn.org/stable/modules/permutation_importance.html) en `sci-kit learn`.
3. [Selección de características](https://topepo.github.io/caret/feature-selection-overview.html) en `caret`.

## Análisis en componentes principales

1. [Notas sobre PCA](https://github.com/mcd-unison/ing-caract/raw/main/pdf/PCA-Standford.pdf) del curso de Andrew Ng en Stanford
2. [Principal Component Analysis](https://jakevdp.github.io/PythonDataScienceHandbook/05.09-principal-component-analysis.html). Libreta de Colab del libro [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)


## Métodos no lineales de reducción de características para visualización

1. [Kernel PCA](https://people.eecs.berkeley.edu/~wainwrig/stat241b/scholkopf_kernel.pdf) con su respectivo [ejemplo en `sci-kit learn`](https://scikit-learn.org/stable/auto_examples/decomposition/plot_kernel_pca.html#sphx-glr-auto-examples-decomposition-plot-kernel-pca-py)
2. [*Manifold learning*](https://scikit-learn.org/stable/modules/manifold.html) en `sci-kit learn`
3. [Libreta de colab sobre *Manifold Learning*](https://jakevdp.github.io/PythonDataScienceHandbook/05.10-manifold-learning.html) del libro [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)
4. [An illustrated introduction to the t-SNE algorithm](https://www.oreilly.com/content/an-illustrated-introduction-to-the-t-sne-algorithm/)
5. [How to Use t-SNE Effectively](https://distill.pub/2016/misread-tsne/)


