# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 16:30:13 2018

load data from https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data
create a file 'adult_dict.json' and store the data as a dictionary

@author: matlab
"""


from urllib.request import urlopen
html = urlopen("https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data")
htmltxt = html.read().splitlines()
datakey = ['age','workplace','fnlwgt','education','education-num','marital-status',
           'occupation','relationship','race','sex','capital-gain','capital-loss',
           'hours-per-week','native-country','income']
list1 = []
d = {}
for i in htmltxt:
    temp = i.decode().split(",")
    if temp == ['']:
        break
    tempdict = dict(zip(datakey, temp))
    list1.append(tempdict)
for k in tempdict.keys():
    d[k] = tuple(d[k] for d in list1)

import json
with open('adult_dict.json','w') as f:
    json.dump(d, f)
