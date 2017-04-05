import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from bokeh.charts import Area, show, output_file, Bar
import operator

data = pd.read_csv("database.csv-", low_memory=False)

year_dist = {}
for year in [1992, 2000, 2015]:
    bydel_dist = {}
    for bydel in range(1, 11):
        tmp_data = data[(data['BYDEL'] == bydel) & (data['AAR'] == year)]
        bydel_dist.update({bydel : sum(tmp_data['PERSONER'])})
    year_dist.update({year : bydel_dist})

max_1992, max_2000, max_2015 = [max(year_dist.get(y).items(), key=operator.itemgetter(1))[0] for y in [1992, 2000, 2015]]

print(max_1992, max_2000)
