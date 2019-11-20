from sklearn.ensemble import RandomForestClassifier
import os
import pickle
import numpy as np
import pandas as pd
from sklearn import datasets

iris = datasets.load_iris()
mapping = dict(zip(np.unique(iris.target), iris.target_names))
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = pd.DataFrame(iris.target).replace(mapping)
model_name = request.data.pop('model_name')
try:
    clf = RandomForestClassifier(**request.data)
    clf.fit(X, y)