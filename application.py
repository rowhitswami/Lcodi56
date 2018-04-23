#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 08:59:37 2018

<<<<<<< HEAD
1.Which product was most sold?
2.What payment modes were used for purchasing products?
3.What is the most common payment method for the United States?
4.What was the earliest time of the day a transaction occurred?
5.Were there repeat customers?

@author: Rohit Swami
=======
@author: rowhit
>>>>>>> 4641e199000311721e0cc3b0905c1d5ea9f13840
"""

import pandas as pd

<<<<<<< HEAD
df = pd.read_csv("dataset.csv")
#print(df.columns)

# Answering First Question
print('Product1 was most sold')
print(df['Product'].value_counts())


# Answering Second Question
payment_method = df['Payment_Type'].unique()
print('\nThe payment modes used for purchasing products:')
for i in range(len(payment_method)):
    print(payment_method[i])
print('\n')

# Answering Third Question
print('\nThe most common payment method for the United States:')
print(df.groupby('Country')['Payment_Type'].value_counts().tail(4))

# Answering Fourth Question
=======
df = pd.read_csv(dataset.csv)
>>>>>>> 4641e199000311721e0cc3b0905c1d5ea9f13840
