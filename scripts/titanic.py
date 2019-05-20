#   https://jorisvandenbossche.github.io/blog/2017/11/20/categorical-encoder/

import pandas as pd
from sklearn.preprocessing import OneHotEncoder

titanic = pd.read_csv("https://raw.githubusercontent.com/amueller/scipy-2017-sklearn/master/notebooks/datasets/titanic3.csv")
titanic = titanic[['pclass', 'sex', 'age', 'sibsp', 'parch', 'fare', 'embarked', 'survived']].dropna()
titanic.head()




encoder = OneHotEncoder(sparse=False)
encoder.fit_transform(titanic[['sex', 'embarked']])
encoder.categories_
