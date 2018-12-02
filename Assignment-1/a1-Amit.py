# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 16:47:27 2017

@author: Amit Warrier
"""

import pandas as pd
import numpy as np


# read data from csv and load data in a dataframe
# Update the path
df = pd.read_csv("patient-data.csv")
print(df)

print(df.groupby(['Race'])["ID"].count())
df['Race'] = np.where(df['Race']=="Dog", None,df['Race'])
print(df.groupby(['Race'])["ID"].count())
print(df[df.Race.isnull()])


print(df.groupby(['Gender'])["ID"].count())
for i in range(0,99):
    df.ix[i,'Gender']=(df.ix[i,'Gender']).strip()
print(df.groupby(['Gender'])['ID'].count())

print(df.groupby(['Smokes'])["ID"].count())
df['Smokes'] = np.where(df['Smokes']=="Yes", "True",df['Smokes'])
df['Smokes'] = np.where(df['Smokes']=="No", "False",df['Smokes'])
print(df.groupby(['Smokes'])["ID"].count())

print(df.groupby(['Pet'])["ID"].count())
df['Pet'] = np.where((df['Pet']=="NONE"), None,df['Pet'])
df['Pet'] = np.where((df['Pet']=="None"), None,df['Pet'])
print(df.groupby(['Pet'])["ID"].count())

print(df.groupby(['HealthGrade'])["ID"].count())
df['HealthGrade'] = np.where((df['HealthGrade']==99), "",df['HealthGrade'])
print(df.groupby(['HealthGrade'])["ID"].count())
df['HealthGrade'] = np.where((df['HealthGrade']=="1"), "Good Health",df['HealthGrade'])
df['HealthGrade'] = np.where((df['HealthGrade']=="2"), "Normal",df['HealthGrade'])
df['HealthGrade'] = np.where((df['HealthGrade']=="3"), "Bad Health",df['HealthGrade'])

print(df.groupby(['Died'])["ID"].count())

df = df.assign(BMI=df['WeightInKgs']/((df['HeightInCms']/100)*(df['HeightInCms']/100)))
print(df)

df = df.assign(BMI_Label="") 
df['BMI_Label'] = np.where(df['BMI']<18.5, 'Underweight',np.where((df['BMI']>=18.5)&(df['BMI']<25), 'Normal',np.where((df['BMI']>=25)&(df['BMI']<30), 'Overweight',"Obese") ) )


#Reporting

print("Top 10 records based on BMI-Value")
print(df.iloc[df['BMI'].nlargest(10).index.values])
print("Bottom 10 records based on BMI-Value")
print(df.iloc[df['BMI'].nsmallest(10).index.values])

print("Frequency / counts of Gender > Race ")
print(df.groupby(['Gender','Race'])["ID"].count())

print("max, min and average values for BMI-Values as per Race > Gender")
print(df.groupby(['Race','Gender'])["BMI"].describe())

print("Records of people who are dead")
print(df[df.Died==True])

print("Records of Hispanic females")
print(df[(df.Gender=="Female") & (df.Race=="Hispanic")])








