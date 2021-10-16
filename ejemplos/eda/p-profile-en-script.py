

#%% Abrir data frame
import pandas as pd
insurance = pd.read_csv("insurance.csv")

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
