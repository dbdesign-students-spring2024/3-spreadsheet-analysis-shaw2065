# Data Set Details
The data set, [New York City Leading Causes of Death](https://data.cityofnewyork.us/Health/New-York-City-Leading-Causes-of-Death/jb7j-dtam/about_data), consists of data on the leading causes of death by sex and ethnicity in New York City since 2007, published and annually updated by the Department of Health and Mental Hygiene. For this exercise, we make use of the JSON format of the original data, converted it into CSV, and analyzed the data through Microsoft Excel.

## Sample raw data (the first 20 rows)

| Year  | Leading Cause | Sex  | Race Ethnicity | Deaths  | Death Rate | Age Adjusted Death Rate |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| 2011  | Nephritis, Nephrotic Syndrome and Nephrisis (N00-N07, N17-N19, N25-N27)  | F  | Black Non-Hispanic  | 83  | 7.9  | 6.9  |
| 2009  | Human Immunodeficiency Virus Disease (HIV: B20-B24)  | F  | Hispanic  | 96  | 8  | 8.1  |
| 2009  | Chronic Lower Respiratory Diseases (J40-J47)  | F  | Hispanic  | 155  | 12.9  | 16  |
| 2008  | Diseases of Heart (I00-I09, I11, I13, I20-I51)  | F  | Hispanic  | 1445  | 122.3  | 160.7  |
| 2009  | Alzheimer's Disease (G30)  | F  | Asian and Pacific Islander  | 14  | 2.5  | 3.6  |
| 2008  | Accidents Except Drug Posioning (V01-X39, X43, X45-X59, Y85-Y86)  | F  | Asian and Pacific Islander  | 36  | 6.8  | 8.5  |
| 2012  | Accidents Except Drug Posioning (V01-X39, X43, X45-X59, Y85-Y86)  | M  | White Non-Hispanic  | 286  | 21.4  | 18.8  |
| 2008  | Assault (Homicide: Y87.1, X85-Y09)  | M  | Not Stated/Unknown  | 8  | -  | -  |
| 2009  | Chronic Lower Respiratory Diseases (J40-J47)  | M  | White Non-Hispanic  | 371  | 27.6  | 23.3  |
| 2013  | Diseases of Heart (I00-I09, I11, I13, I20-I51)  | F  | Not Stated/Unknown  | 106  | -  | -  |
| 2014  | Accidents Except Drug Posioning (V01-X39, X43, X45-X59, Y85-Y86)  | F  | Asian and Pacific Islander  | 42  | 6.7  | 6.9  |
| 2009  | Nephritis, Nephrotic Syndrome and Nephrisis (N00-N07, N17-N19, N25-N27)  | F  | Other Race/ Ethnicity  | -  | -  | -  |
| 2013  | Alzheimer's Disease (G30)  | F  | Hispanic  | 120  | 9.6  | 11  |
| 2011  | Malignant Neoplasms (Cancer: C00-C97)  | F  | Other Race/ Ethnicity  | 33  | -  | -  |
| 2009  | Essential Hypertension and Renal Diseases (I10, I12)  | F  | Hispanic  | 84  | 7  | 8.8  |
| 2007  | Diabetes Mellitus (E10-E14)  | M  | Other Race/ Ethnicity  | 11  | -  | -  |
| 2007  | Cerebrovascular Disease (Stroke: I60-I69)  | M  | White Non-Hispanic  | 267  | 20  | 16.7  |
| 2012  | Accidents Except Drug Posioning (V01-X39, X43, X45-X59, Y85-Y86)  | F  | White Non-Hispanic  | 177  | 12.5  | 8.5  |
| 2007  | Diseases of Heart (I00-I09, I11, I13, I20-I51)  | F  | Not Stated/Unknown  | 82  | -  | -  |
| 2007  | Chronic Lower Respiratory Diseases (J40-J47)  | F  | Hispanic  | 116  | 9.9  | 12.8 |

## Scrubbing task
In the original data, there exist two main issues, while lacking one piece of information we believe is critical to the analysis. Regarding the issues, the first one relates to the disorder of raw data, in which the entire dataset is not ordered based on any pattern, and the second one relates to the commas existing in the leading cause category. Spreadsheets might mistake them for a delimiter, thus resulting in autofilling parts of the text, despite it should be regarded as a whole, into different columns.

To address the first issue, we use the sort_values function in pandas:
```python
sorted_df = df.sort_values(by=['Race Ethnicity', 'Year'], ascending=[True, True])
```
As for the second issue, we put double quotes surrounding data with said problem:
 ```python
if "," in x:
    v = '"' + x + '"'
    x = v
```
The one piece of information we deem missing from the original data is population numbers. Population numbers serve as an indicator of the sex composition of each demographic within the provided data. Additionally, when combined with age adjustment, population numbers could help to deduce the age distribution across different races and ethnicities, allowing for an assessment of susceptibility to specific causes of death across populations of different ages.

To calculate population numbers using data on deaths and death rate, we have code:
```python
sorted_df['Population Number'] = sorted_df['Deaths'] / sorted_df['Death Rate']*1000
```

## Links to data files:
- [New York City Leading Causes of Death](https://data.cityofnewyork.us/Health/New-York-City-Leading-Causes-of-Death/jb7j-dtam/data_preview)
- [Munged Data: New York City Leading Causes of Death](https://github.com/dbdesign-students-spring2024/3-spreadsheet-analysis-shaw2065/blob/main/data/clean_data.csv)
- [Spreadsheet: New York City Leading Causes of Death](https://github.com/dbdesign-students-spring2024/3-spreadsheet-analysis-shaw2065/blob/main/data/clean_data.xlsx)

# Spreadsheet Analysis
## 1. Maximum & Minimum Deaths/ Death Rate/ Age Adjusted Death Rate 
We use the MIN() and MAX() function to find the minimum and maximum value of these three data: deaths, death rate, and age adjusted rate. In order to further examine the data, we use the INDEX() and MATCH() function to return other relevant data in the records of the maximum and minimum values.

## 2. Mean Death Rate of Each Unique Leading Cause of Death for Each Race Ethnicity 

If using a pivot table for analysis, include a Markdown table showing a sample of the results of the pivot table (no more than 20 rows, please), along with a short description of what the results show and any insights they offer.

## 3. Diabetes
![Pivot Chart on Deaths and Death Rate of Diabetes Mellitus](https://github.com/dbdesign-students-spring2024/3-spreadsheet-analysis-shaw2065/blob/main/data/chart.png)

If using a chart for visualization, include the chart image in the report, with a short description of what the image shows and any insights it offers. See the Markdown guide linked above for details of showing an image.

## Extra-credit
This assignment deserves extra credit because we used Python to retrieve the data directly from the webpage using urllib.request instead of downloading the provided CSV file. Additionally, this dataset currently contains a total of 1,094 rows, and we wrote our code to be capable of retrieving a total of 2,000 rows for future updates on the dataset.

