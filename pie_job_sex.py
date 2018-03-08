# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 14:14:54 2018

plot the pie chart for sex and job

@author: matlab
"""

from collections import Counter
import json
import pandas as pd
import matplotlib.pyplot as plt

with open('adult_dict.json') as f:
    d = json.load(f)


indices1 = [i for i, x in enumerate(d['income']) if x == d['income'][0]]
indices2 = [i for i, x in enumerate(d['income']) if x == d['income'][9]]


above_sex = []
below_sex = []
for i in indices1:
    below_sex.append(d['sex'][i])
for i in indices2:
    above_sex.append(d['sex'][i])
    
above_job = []
below_job = []
for i in indices1:
    below_job.append(d['occupation'][i])
for i in indices2:
    above_job.append(d['occupation'][i])

my_count = pd.Series(above_sex).value_counts() 
plt.figure()  
my_count.plot(kind='pie', title = 'above50k: sex') 
plt.axis('equal')
my_count = pd.Series(below_sex).value_counts() 
plt.figure() 
my_count.plot(kind='pie', title = 'below50k: sex') 
my_count = pd.Series(d['sex']).value_counts() 
plt.figure() 
my_count.plot(kind='pie', title = 'total: sex') 


my_count = pd.Series(above_job).value_counts() 
plt.figure() 
my_count.plot(kind='pie', title = 'above50k: job') 
plt.axis('equal')
my_count = pd.Series(below_job).value_counts() 
plt.figure() 
my_count.plot(kind='pie', title = 'below50k: job') 
my_count = pd.Series(d['occupation']).value_counts() 
plt.figure() 
my_count.plot(kind='pie', title = 'total: job') 
plt.figure() 



