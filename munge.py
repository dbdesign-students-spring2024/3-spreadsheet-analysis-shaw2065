# place your code to clean up the data file below.
import urllib.request
import json
import pandas as pd

source = urllib.request.urlopen('https://data.cityofnewyork.us/resource/jb7j-dtam.json?$limit=2000')
data = json.load(source)

w = open("./data/clean_data.csv", "w")

headings = list(data[0].keys())
heading = []
for h in headings:
    s = ""
    for char in h:
        if char == "_":
            s += " "
        else:
            s += char
    headings[headings.index(h)] = s.title()
w.write(",".join(headings))
w.write("\n")

starting = True
for i in data:
    for x in i.values():
        if starting:
            w.write(x)
            starting = False
        else:
            if "," in x:
                v = ""
                v = '"' + x + '"'
                x = v
            w.write(","+x)
    w.write("\n")
    starting = True

w.close()

df = pd.read_csv("./data/clean_data.csv")

#sort the DataFrame by 'Race Ethnicity' and then by 'Year' in ascending order
sorted_df = df.sort_values(by=['Race Ethnicity', 'Year'], ascending=[True, True])

sorted_df['Deaths'] = pd.to_numeric(sorted_df['Deaths'], errors='coerce')
sorted_df['Death Rate'] = pd.to_numeric(sorted_df['Death Rate'], errors='coerce')
sorted_df['Age Adjusted Death Rate'] = pd.to_numeric(sorted_df['Age Adjusted Death Rate'], errors='coerce')
sorted_df['Population Number'] = sorted_df['Deaths'] / sorted_df['Death Rate']*1000

#remove the original 'Death Rate' column so that it can be recalculated later
sorted_df.drop('Death Rate', axis=1, inplace=True)

#if 'Leading Cause', 'Sex', 'Race Ethnicity' are all the same, then combine these rows by summing 'Deaths' and 'Population Number'
grouped_df = sorted_df.groupby(['Year','Leading Cause', 'Sex', 'Race Ethnicity']).agg({
    'Deaths': 'sum',
    'Population Number': 'sum',
    'Age Adjusted Death Rate': 'sum'
}).reset_index()

#recalculate the death rate
grouped_df['Death Rate'] = (grouped_df['Deaths'] / grouped_df['Population Number']) * 1000
grouped_df['Population Number'] = grouped_df['Population Number'].round(1)
grouped_df['Death Rate'] = grouped_df['Death Rate'].round(1)
grouped_df.insert(7, 'Age Adjusted Death Rate', grouped_df.pop('Age Adjusted Death Rate'))

import numpy as np
#replace 0.0 values with NaN
grouped_df['Deaths'] =grouped_df['Deaths'].replace(0, np.nan)
grouped_df['Population Number'] =grouped_df['Population Number'].replace(0, np.nan)
grouped_df['Death Rate'] =grouped_df['Death Rate'].replace(0, np.nan)
grouped_df['Age Adjusted Death Rate'] =grouped_df['Age Adjusted Death Rate'].replace(0, np.nan)
#also replace infinity values with NaN
grouped_df.replace([np.inf, -np.inf],np.nan,inplace=True)

grouped_file_path = './data/clean_data.csv'
grouped_df.to_csv(grouped_file_path, index=False)

unique_values = grouped_df['Leading Cause'].unique()
print(unique_values)