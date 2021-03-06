#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 08:59:37 2018

1.Which product was most sold?
2.What payment modes were used for purchasing products?
3.What is the most common payment method for the United States?
4.What was the earliest time of the day a transaction occurred?
5.Were there repeat customers?

@author: Rohit Swami
"""

import pandas as pd

df = pd.read_csv("dataset.csv")
#print(df.columns)

# Removing space from City column
df['Name'] = df['Name'].str.capitalize()
df['City'] = df['City'].map(lambda x: x.rstrip(' '))
df['City'] = df['City'].map(lambda x: x.lstrip(' '))

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
print('\n Earliest time of the day when a transaction occured:')
df['Transaction_date'] = pd.to_datetime(df['Transaction_date'])
sorted_date = df.sort_values('Transaction_date')
earliest_time = sorted_date[~sorted_date['Transaction_date'].dt.date.duplicated()]
print(earliest_time['Transaction_date'])

# Answering Fifth Question
print('\nAs the value_counts() function of the below line is returning no value greater than 1, it shows that every customer, even if they have same name, have bought product only once. So it means there are no repeat customers in this span of time.\n')
#print(df.groupby('Name')['City'].value_counts(ascending=False))

