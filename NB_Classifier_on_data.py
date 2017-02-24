import pandas as pd
import numpy as np
from sklearn.naive_bayes import GaussianNB

X = pd.read_csv("dataframe.csv") #Reads from the csv posted

gnb = GaussianNB() #Sets the guassian Naive Bayes Classifier

Y = X['labels'] #Setting Y

del X['labels']
del X['travelClass']  #These two remove these specified columns from db


y_pred = gnb.fit(X,Y).predict(X)  #predicted Y

print "Error on total points is: "
print (Y != y_pred).sum()*1.0/len(X) #Calculates error
