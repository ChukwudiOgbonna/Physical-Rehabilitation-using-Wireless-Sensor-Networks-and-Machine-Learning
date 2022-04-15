import concurrent
import sqlite3
import concurrent.futures
import datetime
import executor as executor
import numpy as np
import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix
class ML:
    def __init__(self):
        from sklearn.preprocessing import LabelEncoder, OneHotEncoder

        data = pd.read_csv('/Users/chuks/Downloads/dataset.csv')
        #print(data.head())
        X = data.drop('MOTOR IMPAIRMENT', axis=1)

        y = data['MOTOR IMPAIRMENT']
        label_encoder = LabelEncoder()
        integer_encoded = label_encoder.fit_transform(y)
        #print(integer_encoded)
        new_series = pd.Series(integer_encoded)

        from sklearn.model_selection import train_test_split

        X_train, X_test, y_train, y_test = train_test_split(X, new_series, test_size=0.2, random_state=15)
        from sklearn.naive_bayes import GaussianNB
        model = GaussianNB()
        model.fit(X_train, y_train)
        y_pred4= model.predict(X_test)


        from sklearn.svm import SVC
        svclassifier = SVC(kernel='linear')
        svclassifier.fit(X_train, y_train)
        y_pred = svclassifier.predict(X_test)


        np_array = np.array([1, 0, 0, 1, 0, 0, 1, 0, 1, 0])
        np_array = np_array.reshape(1, -1)
        answer = svclassifier.predict(np_array)
        #print(answer)
        self.model=svclassifier
        #print(classification_report(y_pred,y_test))

        # 0- Arthritis
        # 1- Cerebral Palsy
        # 2- Left Sided stroke
        # 3- None
        # 4- Parkinson Disease
        # -Right Sided stroke
    def getModel(self):
        return self.model

model= ML()


