import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("database.csv-", low_memory=False)
data_18_plus = data[data['ALDER'] > 17]
statuses = {'E' : 'Enke/-mand', 'F' : 'Fraskilt', 'G' : 'Gift', 'L' : 'Længstlevende partner', 'O' : 'Ophævet partnerskab', 'P' : 'Registreret partnerskab', 'U' : 'Ugift'}
year_dict = [data_18_plus[data_18_plus['AAR'] == year] for year in range(1992, 2015)]

distribution = {}
for status in statuses:
    year_dist = {}
    for year in year_dict:
        var = year.loc[year['CIVST'] == status]
        var_sum = sum(var['PERSONER'])
        all_sum = sum(year['PERSONER'] )
        year_dist.update({ int(year.head(1)['AAR']) : var_sum / all_sum * 100 })
    distribution.update({ status : year_dist})

fig, ax = plt.subplots()
for status in statuses:
    ds_x, ds_y =  zip(*sorted(distribution.get(status).items()))
    ax.plot(ds_x, ds_y, label=statuses.get(status))

legend = ax.legend(loc='upper center', shadow=False)
frame = legend.get_frame()
plt.xlabel('Year', fontsize=16)
plt.ylabel('Percent of Population', fontsize=16)
plt.title('Fordeling af Civilstatus fra 1992 til 2015 i Procent')

plt.show()
