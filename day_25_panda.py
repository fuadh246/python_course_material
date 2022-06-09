import pandas as pd
import numpy as np
print()
print('Creating DataFrames from List of Lists')
data = [
    ['Asabeneh', 'Finland', 'Helsink'], 
    ['David', 'UK', 'London'],
    ['John', 'Sweden', 'Stockholm']
]
df = pd.DataFrame(data, columns=['Names','Country','City'])
print(df)
print()
print('Creating DataFrame Using Dictionary')
data = {'Name': ['Asabeneh', 'David', 'John'], 'Country':[
    'Finland', 'UK', 'Sweden'], 'City': ['Helsiki', 'London', 'Stockholm']}
df = pd.DataFrame(data)
print(df)
print()
print('Creating DataFrames from a List of Dictionaries')
data = [
    {'Name': 'Asabeneh', 'Country': 'Finland', 'City': 'Helsinki'},
    {'Name': 'David', 'Country': 'UK', 'City': 'London'},
    {'Name': 'John', 'Country': 'Sweden', 'City': 'Stockholm'}]
df = pd.DataFrame(data)
print(df)
print()
df=pd.read_csv('weight-height.csv')
print(df)
print()
print(df.head())
print()
print(df.tail()) 
print()
print('Shape: ',df.shape)
print('columns: ',df.columns)
print()
heights = df['Height']
print(heights)
print('mean of heights ->',heights.mean())
print()
print(heights.describe())
print()
print(df.describe())

df=pd.read_csv('hacker_news.csv')
print(df.columns)
url=df['url']
print(url.head())
