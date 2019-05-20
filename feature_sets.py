import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import csv
from pylab import rcParams
get_ipython().magic('matplotlib inline')
# графики в svg выглядят более четкими
get_ipython().magic("config InlineBackend.figure_format = 'svg'")
# увеличим дефолтный размер графиков
rcParams['figure.figsize'] = 8, 5
df = pd.read_excel('pairs.xlsx', index_col = 0, decimal = ",")
df['weight1'] = df.weight1.astype('float64') 
df['weight2'] = df.weight2.astype('float64')

fig, ax = plt.subplots()

colors = {'Lasso_vs_SelectKBest':'blue', 'Lasso_vs_RFE':'orange', 'Lasso_vs_SCAD':'green', 
         'Lasso_vs_QuiPT':'red', 'SelectKBest_vs_RFE':'purple', 'SelectKBest_vs_SCAD':'brown', 
         'SelectKBest_vs_QuiPT':'pink', 'RFE_vs_SCAD':'grey', 'RFE_vs_QuiPT':'lime', 
         'SCAD_vs_QuiPT':'cyan' }

grouped = df.groupby('pair')
for key, group in grouped:
    group.plot(ax = ax, kind = 'scatter', x = 'weight1', y = 'weight2', label = key, 
	      color = colors[key])

plt.show()
fig.savefig("weights.pdf")


