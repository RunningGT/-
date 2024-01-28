import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
titanic = pd.read_csv('train.csv')
# print(titanic.head())
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
print(titanic.describe())
# 打印 'Sex' 和 'Embarked' 列的描述性统计信息
print(titanic[['Sex', 'Embarked']].describe())

titanic['Age'] = titanic['Age'].fillna(titanic['Age'].median())
titanic.loc[titanic['Sex'] == 'male', 'Sex'] = 0
titanic.loc[titanic['Sex'] == 'female', 'Sex'] = 1

titanic['Embarked'] = titanic['Embarked'].fillna('S')
titanic.loc[titanic['Embarked'] == 'S', 'Embarked'] = 0
titanic.loc[titanic['Embarked'] == 'C', 'Embarked'] = 1
titanic.loc[titanic['Embarked'] == 'Q', 'Embarked'] = 2

print(titanic.describe())
print(titanic[['Sex', 'Embarked']].describe())
