"""
Lab_2.py: Read and process LendingClub loan data

Created on Wed Jul 29 21:50:33 2015

@author: mr.statsguy@gmail.com
"""

#To set up -
#1) download data from link below -
#https://resources.lendingclub.com/RejectStatsB.csv.zip

#2) Second, we will run the code below -read in and process this file. 


import csv
import numpy
import matplotlib.pyplot as plt

inFile = '/Users/timothyliu/LendingClub/RejectStatsB.csv'

f = open(inFile, 'rb')
f.next()
f.next()

reader = csv.reader(f)

ctr = 0

d = {}

for row in reader:
    ctr += 1
    if ctr == 500: break
    AmountRequested,ApplicationDate,LoanTitle,FICOScore,DebtToIncomeRatio,Zip,State,EmploymentLength,PolicyCode = row

    DebtToIncomeRatio = 0.01 * float(DebtToIncomeRatio.strip('%'))

    try:
        FICOScore = int(FICOScore)
    except ValueError as e:
        continue
    
    if State not in d:
        d[State] = []
    d[State].append(FICOScore)
    
f.close()

for State in sorted(d):
    print State, len(d[State]), numpy.mean(d[State])


n, bins, patches = plt.hist(d['TX'], 50, normed=1, facecolor='g')
plt.xlabel('TX')
plt.ylabel('Distribution')
plt.title('Histogram of Fico Score')
plt.show()


