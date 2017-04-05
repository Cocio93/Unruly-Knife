import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("database.csv-", low_memory=False)

data_years = [data[data['AAR'] == year] for year in range(1992, 2015)]

data_dict = {}
for entry in data_years:
    year_dict = {}
    year = int(entry.head(1)['AAR'])
    for i in range(0, 10):
        tmp = entry[entry['BYDEL'] == i]
        year_dict.update({ i : sum(tmp['PERSONER'])})
    data_dict.update({ year : year_dict})

fig, ax = plt.subplots()
for 
