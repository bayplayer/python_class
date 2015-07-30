

#========> Ex 1. Compute summary statistics across records <============

import numpy as np
        
#raw data -4 columns: date, custoNo, merchant, amt
data_lines = '''2012-12-28,10001,best buy,120.89
2013-01-09,10001,netflix, 9.99
2013-05-28,10001,1-800 Flowers,89.99
2014-01-03,10002,google play, 2.99
2014-01-10,10002,amazon, 34.90
2013-09-18,10003,macys, 65.27
2013-11-24,10003,walmart,249.95
2014-01-12,10004,burger king,14.97'''


#initialize a list to hold values of transaction amount
ls_amount = []

#parse data

lines = data_lines.split('\n')
for line in lines:
    txnDate, customerId, merchant, amount = line.split(',')
    amount = float(amount)
    ls_amount.append(amount)

 
print 'The Avg Txn Amount is %f' %np.mean(ls_amount) 

