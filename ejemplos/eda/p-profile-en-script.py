

#%% Abrir data frame
import pandas as pd
url_insurance = "https://github.com/mcd-unison/ing-caract/raw/main/ejemplos/eda/insurance.csv"
url_titanic = "https://github.com/mcd-unison/ing-caract/raw/main/ejemplos/eda/titanic.csv"
insurance = pd.read_csv(url_insurance)

#%% Probando pandas-profiling

from pandas_profiling import ProfileReport 

profile = ProfileReport(
    insurance, 
    explorative=True,
    title='Reporte de insurance.csv', 
    html={'style':{'full_width':True}}
) 
profile.to_file("insurance-pandas-profiler.html")

#%% Probando Sweetview

import sweetviz

sw_insurance = sweetviz.analyze(insurance)
sw_insurance.show_html("insurance-sweetview.html")
