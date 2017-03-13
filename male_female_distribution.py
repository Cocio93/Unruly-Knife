import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("database.csv-", low_memory=False)

def get_age_interval(start, end, gender):
    return gender[(gender['ALDER'] > start) & (gender['ALDER'] < end)]

def make_plottable(dataset):
    out_dict = {}
    for entry in dataset:
        out_dict.update({int(entry.head(1)['AAR']) : sum(entry['PERSONER'])})

    return zip(*sorted(out_dict.items()))

def distribute_by_year(dataset):
    return [dataset[dataset['AAR'] == year] for year in range(1992, 2015)]

def plot_dataslice(dataslice, label):
    ds_x, ds_y =  make_plottable(dataslice)
    ax.plot(ds_x, ds_y, label=label)

## Seperate Men and Women
men, women = [data[data['KOEN'] == sex] for sex in [1, 2]]

## Divide Men and Women into young and old
young_men, young_women = [get_age_interval(17, 30, sex) for sex in [men, women]]
old_men, old_women = [get_age_interval(50, 99, sex) for sex in [men, women]]

#¤ Divide datasets into dictionary with Year as Key, and amount of people from the category living in the city that year
men_dist, women_dist, old_men_dist, old_women_dist = [distribute_by_year(cat) for cat in [young_men, young_women, old_men, old_women]]

## Finally Prepare the plot and show it
fig, ax = plt.subplots()
plot_dataslice(men_dist, "Males, 18-30")
plot_dataslice(women_dist, "Females, 18-30")
plot_dataslice(old_men_dist, "Males, 50+")
plot_dataslice(old_women_dist, "Females, 50+")

legend = ax.legend(loc='upper center', shadow=False)
frame = legend.get_frame()

plt.xlabel('Year', fontsize=16)
plt.ylabel('Count', fontsize=16)
plt.title('Fordeling af indbyggere i København og Omegn')

plt.show()
