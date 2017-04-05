import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from bokeh.charts import Area, show, output_file, Bar

statuses = {'E' : 'Enke/-mand', 'F' : 'Fraskilt', 'G' : 'Gift', 'L' : 'Længstlevende partner', 'O' : 'Ophævet partnerskab', 'P' : 'Registreret partnerskab', 'U' : 'Ugift'}
singles = ['E', 'F', 'L', 'O', 'U']

data = pd.read_csv("database.csv-", low_memory=False)
data = data[(data['ALDER'] > 17) & (data['ALDER'] < 31) & (data['BYDEL'] < 4) & data['CIVST'].isin(singles)]

distribution = {}
for bydel in range(1,4):
    bydel_dist = {}
    for year in range(1992, 2015):
        tmp_data = data[(data['BYDEL'] == bydel) & (data['AAR'] == year)]
        bydel_dist.update({ year : sum(tmp_data['PERSONER'])})
    distribution.update({bydel : bydel_dist})

index = [i for i in range(1992, 2015)]
bar_width = 0.35
for title, data_dict in distribution.items():
    x = list(data_dict.keys())
    y = list(data_dict.values())
    plt.figure()
    plt.bar(index, y, bar_width,
                 alpha=0.8,
                 color='b',
                 yerr=x,
                 error_kw= {'ecolor': '0.3'},
                 label=title)
    plt.title(title)

plt.legend()
plt.tight_layout()
plt.show()
