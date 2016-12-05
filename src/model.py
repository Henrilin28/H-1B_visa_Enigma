import os
import seaborn as sns
import sklearn as sl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier

from cat_data import dummyEncode, plot_cat_info
from misc import uni_wage,generate_list


def read_data():
    H1B_data = pd.read_csv('enigma-h1b.csv')
    dfcat = H1B_data[['lca_case_employer_name',
           'lca_case_employer_address', 'lca_case_employer_city',
           'lca_case_employer_state', 'lca_case_employer_postal_code',
           'lca_case_soc_code', 'lca_case_soc_name', 'lca_case_job_title',
           'lca_case_wage_rate_unit', 'full_time_pos',
            'lca_case_workloc1_city', 'lca_case_workloc1_state']]
    dfcat_dummy = dummyEncode(dfcat)
    data = pd.concat([dfcat_dummy,H1B_data[['lca_case_wage_rate_from',
                                            'lca_case_wage_rate_to', 'total_workers',
                                            'status']]],axis=1)
    data = data.fillna(0)

    return data

def model(data):
    data['is_train'] = np.random.uniform(0, 1, len(data)) <= .75

    train, test = data[data['is_train']==True], data[data['is_train']==False]

    idx = ['is_train',"status"]
    features = [i for j, i in enumerate(list(data.columns.values)) if i not in idx]
    #clf = RandomForestClassifier(n_jobs=100)
    clf = svm.SVC(cache_size=7000)
    y, _ = pd.factorize(train['status'])
    clf.fit(train[features], y)

    preds = data.status[clf.predict(test[features])]
    print pd.crosstab(test['status'], preds, rownames=['actual'],
                      colnames=['preds'])

if __name__ == '__main__':

    data = read_data()

    data_part = data.sample(1000)

    model(data)
