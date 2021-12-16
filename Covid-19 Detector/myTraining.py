import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
import pickle

def data_split(data, ratio):
    test_set_size = int(len(data) * ratio)
    test_data = data[:test_set_size]
    train_data = data[test_set_size:]
    return  train_data, test_data


if __name__ == "__main__":

    
    df = pd.read_csv('data.csv')
    train, test = data_split(df, 0.2)
    X_train = train[['fever', 'bodyPain', 'age', 'runnyNose', 'diffBreath']].to_numpy()
    X_test = test[['fever', 'bodyPain', 'age', 'runnyNose', 'diffBreath']].to_numpy()

    Y_train = train[['infectionProb']].to_numpy().reshape(2060 ,)
    Y_test = test[['infectionProb']].to_numpy().reshape(515 ,)

    clf = LogisticRegression()
    clf.fit(X_train, Y_train)

    
    file = open('model.pkl', 'wb')

   
    pickle.dump(clf, file)
    file.close()




