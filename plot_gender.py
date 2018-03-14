# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 14:37:55 2018

@author: matlab
"""

from collections import Counter
import json
import matplotlib.pyplot as plt
#import seaborn as sns

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

#plot above_sex

counts = Counter(above_sex)
colors = ['lightskyblue', 'lightcoral']
explode = (0.1, 0)
patches, texts, autotexts = plt.pie([float(v) for v in counts.values()], labels=counts.keys(), colors=colors, 
         autopct='%1.1f%%', shadow=True, startangle=100, explode = explode)
texts[0].set_fontsize(18)
texts[1].set_fontsize(18)
autotexts[0].set_fontsize(18)
autotexts[1].set_fontsize(18)
plt.axis('equal')
plt.title('Income above 50K Dollars', fontsize = 25)
plt.savefig("pie_sex_above50k.png")

#plot below_sex
plt.figure()
counts = Counter(below_sex)
colors = ['lightskyblue', 'lightcoral']
explode = (0.1, 0)
patches, texts, autotexts = plt.pie([float(v) for v in counts.values()], labels=counts.keys(), colors=colors, 
         autopct='%1.1f%%', shadow=True, startangle=100, explode = explode)
texts[0].set_fontsize(18)
texts[1].set_fontsize(18)
autotexts[0].set_fontsize(18)
autotexts[1].set_fontsize(18)
plt.axis('equal')
plt.title('Income below 50K Dollars', fontsize = 25)
plt.savefig("pie_sex_below50k.png")







