# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 16:27:27 2017

@author: Amit Warrier
"""

import pandas as pd
import numpy as np
import math
#reading data file
df = pd.read_csv("G:/Python/26417/weather-data.csv")

# view Data
print(df.head())
# check Column Names
print(df.columns)
#Count of NA Readings in each column
df.isnull().sum()
for i in range(0,153):
    if math.isnan(df.iloc[i,2])==True:
        j=i
        while(math.isnan(df.iloc[j,2])==True):
            j=j+1
            print(j)
        df.iloc[i,2]=np.mean((df.ix[(i-1),'Ozone'],df.ix[j,'Ozone']))
        
for i in range(0,153):
    if math.isnan(df.iloc[i,3])==True:
        j=i
        while(math.isnan(df.iloc[j,3])==True):
            j=j+1
            print(j)
        df.iloc[i,3]=np.mean((df.ix[(i-1),'Solar'],df.ix[j,'Solar']))

for i in range(0,153):
    if math.isnan(df.iloc[i,4])==True:
        df.iloc[i,4]=np.mean(df.iloc[range(max(i-5,0),min(i+6,152)),4])
        
        
for i in range(0,153):
    if math.isnan(df.iloc[i,5])==True:
        df.iloc[i,5]=np.mean(df.iloc[range(max(i-5,0),min(i+6,152)),5])
        
tempdict={'a':'Very Hot','b':'hot','c':'mild','d':'cool','e':'cold'}
winddict={'a':'storm','b':'windy','c':'breezy','d':'slow wind','e':'still'}
df=df.assign(weather="")
for i in range(0,153):
    if df.ix[i,'Wind']<=np.percentile(df['Wind'],20):
        df.ix[i,'weather'] =winddict['e']

    elif (df.ix[i,'Wind']<=np.percentile(df['Wind'],40)):
        df.ix[i,'weather'] =winddict['d']

    elif (df.ix[i,'Wind']<=np.percentile(df['Wind'],60)):
        df.ix[i,'weather'] =winddict['c']

    elif (df.ix[i,'Wind']<=np.percentile(df['Wind'],80)):
        df.ix[i,'weather'] =winddict['b']

    elif (df.ix[i,'Wind']<=np.percentile(df['Wind'],100)):
        df.ix[i,'weather'] =winddict['a']

for i in range(0,153):
    if df.ix[i,'Temp']<=np.percentile(df['Temp'],20):
        df.ix[i,'weather'] +=" & "+tempdict['e']

    elif (df.ix[i,'Temp']<=np.percentile(df['Temp'],40)):
        df.ix[i,'weather'] +=" & "+tempdict['d']

    elif (df.ix[i,'Temp']<=np.percentile(df['Temp'],60)):
        df.ix[i,'weather'] +=" & "+tempdict['c']

    elif (df.ix[i,'Temp']<=np.percentile(df['Temp'],80)):
        df.ix[i,'weather'] +=" & "+tempdict['b']

    elif (df.ix[i,'Temp']<=np.percentile(df['Temp'],100)): 
        df.ix[i,'weather']+=" & "+tempdict['a']
