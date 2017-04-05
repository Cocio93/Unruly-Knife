import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from bokeh.charts import Area, show, output_file, Bar
import operator

data = pd.read_csv("database.csv-", low_memory=False)
data = data[data['AAR'] == 2015][['ALDER', 'PERSONER']]

ages = data['ALDER'].unique()

age_dict = {}
for age in ages:
    tmp_data = data[data['ALDER'] == age]
    age_dict.update({age : sum(tmp_data['PERSONER'])})
print(age_dict)
