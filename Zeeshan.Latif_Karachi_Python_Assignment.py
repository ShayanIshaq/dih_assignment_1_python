# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 09:36:51 2017

@author: Zeeshan.Latif
"""

import pandas
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')

df=pandas.read_csv("E:/DIH/chronic_kidney_disease_updated.csv")

#print column names
print(list(df) )

#print first 5 rows
print(df.head())

df.drop(df.index[[0]], inplace=True)
#df.drop('Unnamed: 0', axis=1, inplace=True)

print(df.dm.unique() )

def replace(tup, df):
    for i in tup:
        df.replace(to_replace=i, value=np.nan, inplace=True)
        
def cleandf(df):
   df=df.applymap(lambda x: str(x).strip())
   return df
    
df=cleandf(df)
    
replace(( "\t", " ", "?"), df)

print(df.dm.unique() )

numeric_columns= ['age', 'bp', 'bgr', 'bu', 'sc', 'sod', 'pot', 'hemo', 'pcv', 'wbcc', 'rbcc']
for i in numeric_columns:
   df[i] = pandas.to_numeric(df[i], errors='coerce')


print(df[['pc','al']])

df.rename(columns={'class': 'Class'}, inplace=True)
ckd=df[df.Class=='ckd']

normal_count=(len(ckd[ckd.rbc=='normal'].index))
abnormal_count=(len(ckd[ckd.rbc=='abnormal'].index))

ckd['rbc'].value_counts().plot(kind='bar')

#x_pos=np.array('normal','abnormal')
#y_pos=np.array(normal_count, abnormal_count)

print(ckd['bp'].max())


df.to_csv(path_or_buf="E:/DIH/clean_chronic_kidney_disease.csv")
