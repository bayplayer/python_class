"""
bioResponse.py: Predict a biological response of molecules from their chemical properties

Created on Wed Jul 29 21:50:33 2015

@author: mr.statsguy@gmail.com
"""

"""
To set up -
1) download data from link below -
https://www.kaggle.com/c/bioresponse/data

2) Second, we will run the code below to build a RF model
"""


'''
https://www.kaggle.com/c/bioresponse/data
'''


from sklearn.ensemble import RandomForestClassifier
import csv_io

def main():
    train = csv_io.read_data("Data/train.csv")
    target = [x[0] for x in train]
    train = [x[1:] for x in train]
    test = csv_io.read_data("Data/test.csv")

    rf = RandomForestClassifier(n_estimators=100)
    rf.fit(train, target)
    predicted_probs = rf.predict_proba(test)
    predicted_probs = ["%f" % x[1] for x in predicted_probs]
    csv_io.write_delimited_file("Data/rf_benchmark.csv",
                                predicted_probs)

if __name__=="__main__":
    main()
