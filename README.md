## Using python and the attached data store, answer the following questions:

### 1. Which product was most sold?
![Bar Chart](https://github.com/rowhitswami/Lcodi56/blob/master/img/1.svg)

### 2. What payment modes were used for purchasing products?
* MasterCard
* Visa
* Diners
* Amex


### 3. What is the most common payment method for the United States?
![Bar Chart](https://github.com/rowhitswami/Lcodi56/blob/master/img/2.svg)

### 4. What was the earliest time of the day a transaction occurred?
2009-01-01 01:26:00

2009-01-02 00:50:00

2009-01-03 06:41:00

2009-01-04 01:05:00

2009-01-05 00:31:00

2009-01-06 01:20:00

2009-01-07 00:12:00

2009-01-08 00:04:00

2009-01-09 01:12:00

2009-01-10 00:04:00

2009-01-11 00:15:00

2009-01-12 00:17:00

2009-01-13 01:46:00

2009-01-14 00:03:00

2009-01-15 01:41:00

2009-01-16 01:07:00

2009-01-17 01:23:00

2009-01-18 00:41:00

2009-01-19 01:52:00

2009-01-20 02:17:00

2009-01-21 02:07:00

2009-01-22 02:16:00

2009-01-23 03:30:00

2009-01-24 01:22:00

2009-01-25 00:09:00

2009-01-26 01:14:00

2009-01-27 02:26:00

2009-01-28 00:22:00

2009-01-29 01:01:00

2009-01-30 01:09:00

2009-01-31 01:59:00

### 5. Were there repeat customers? Discuss possible issues. 
First I took “Name” and “Country” into consideration to find out the repeat
customers. But there could be two person with same name and same city. So this
time I took “Name” and “City”, and found out that there are no repeat customers.

Technical Definition:

```python
  df.groupby('Name')['City'].value_counts(ascending=False)
```

As the value_counts() function of the above line is returning no value greater than 1, it
shows that every customer, even if they have same name, have bought product only
once. So it means there are no repeat customers in this span of time.


- [x] Due Date: Between April 22 - April 26, 2018. 
