# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 15:44:25 2018

@author: matlab
"""


import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import string
import seaborn as sns

names =['age','workplace','fnlwgt','education','working-num','marital-status',
           'occupation','relationship','race','sex','capital-gain','capital-loss',
           'hours-per-week','native-country','income']
df_train = pd.read_csv('adult.data.txt',header=None,names=names)
df_over = df_train[df_train['income']==' >50K']
df_und = df_train[df_train['income']==' <=50K']
total_over = float(len(df_over['occupation']))
total_und = float(len(df_und['occupation']))

#plot above 50k for ocupation
plt.figure(figsize=(20,10))
ax = sns.countplot(x = df_over['occupation'], order = df_over['occupation'].value_counts().iloc[:7].index,
              orient = 'v',palette=sns.color_palette("husl", 7))
plt.title('Top 7 job types above 50k', fontsize = 25)
plt.xlabel('Category Name', fontsize = 20)
plt.ylabel('Count of Item in the Category', fontsize = 20)
plt.tick_params(labelsize = 18)
#plt.savefig('top_10_cat.png', bbox_inches='tight')
for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x()+p.get_width()/2.,
            height + 3,
            '{:.2f}%'.format((height/total_over)*100), fontsize = 20,
            ha="center") 
plt.savefig('top_8_above_job.png')
plt.show()

#plot below 50k for ocupation
plt.figure(figsize=(20,10))
ax = sns.countplot(x = df_und['occupation'], order = df_und['occupation'].value_counts().iloc[:7].index,
              orient = 'v',palette=sns.color_palette("husl", 7))
plt.title('Top 7 job types below 50k', fontsize = 25)
plt.xlabel('Category Name', fontsize = 20)
plt.ylabel('Count of Item in the Category', fontsize = 20)
plt.tick_params(labelsize = 18)

for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x()+p.get_width()/2.,
            height + 3,
            '{:.2f}%'.format((height/total_und)*100), fontsize = 20,
            ha="center") 
plt.savefig('top_8_below_job.png')
plt.show()

total = float(len(df_train.sex))

plt.figure(figsize=(10,10))
ax = sns.countplot(df_train.sex,palette=sns.xkcd_palette(['sky blue', 'blush pink']))
plt.title('Gender distribution for whole dataset', fontsize = 25)
plt.ylabel('Count of item', fontsize = 20)
plt.xlabel('Sex', fontsize = 20)

for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x()+p.get_width()/2.,
            height + 3,
            '{:.2f}%'.format((height/total)*100), fontsize = 20,
            ha="center") 
    
plt.tick_params(labelsize = 18)
#plt.savefig('shipping.png', bbox_inches='tight')
plt.show()
