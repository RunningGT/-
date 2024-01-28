import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 加载数据集
data = pd.read_csv('train.csv')

# 数据预处理(暂时用不到，但我还是给他加上，方便后面增加统计功能)
# 填充年龄列的缺失值
data['Age'] = data['Age'].fillna(data['Age'].median())

# 将性别列转换为数值型，男性为0，女性为1
data.loc[data['Sex'] == 'male', 'Sex'] = 0
data.loc[data['Sex'] == 'female', 'Sex'] = 1

# 填充 Embarked 列的缺失值
data['Embarked'] = data['Embarked'].fillna('S')

# 将 Embarked 列转换为数值型，S为0，C为1，Q为2
data.loc[data['Embarked'] == 'S', 'Embarked'] = 0
data.loc[data['Embarked'] == 'C', 'Embarked'] = 1
data.loc[data['Embarked'] == 'Q', 'Embarked'] = 2

# 打印处理后的数据统计信息
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
print(data.describe())
print(data[['Sex', 'Embarked']].describe())

# 设置 seaborn 风格
sns.set_style("whitegrid")

# 生成生还率的饼状图
survival_rate = data['Survived'].value_counts(normalize=True)
labels = ['Died', 'Survived']
sizes = [1 - survival_rate[1], survival_rate[1]]
explode = (0, 0.1)  # 突出显示生还者部分
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Survival Rate by Survival Status')
plt.savefig("Titanic(1).png")
plt.show()

# 分析Pclass（船舱等级）对生还率的影响
pclass_survival = data.groupby('Pclass')['Survived'].mean()
pclass_survival = pclass_survival.sort_index()

# 创建条形图
sns.barplot(x=pclass_survival.index, y=pclass_survival.values, palette='viridis')
plt.title('Survival Rate by Pclass')
plt.xlabel('Pclass')
plt.ylabel('Survival Rate')

for X, Y in zip(pclass_survival.index, pclass_survival.values):
    plt.text(X - 1, Y + 0.005, '%.2f' % Y, ha='center', va='bottom')

plt.savefig("Titanic(2).png")
plt.show()

# 分析性别对生还率的影响
sex_survival = data.groupby('Sex')['Survived'].mean()
sex_survival = sex_survival.sort_index()

# 创建条形图
sns.barplot(x=sex_survival.index, y=sex_survival.values, palette='viridis')
plt.title('Survival Rate by Gender')
plt.xlabel('Gender')
plt.ylabel('Survival Rate')

for X, Y in zip(sex_survival.index, sex_survival.values):
    plt.text(X, Y + 0.005, '%.2f' % Y, ha='center', va='bottom')

plt.savefig("Titanic(3).png")
plt.show()

# 分析年龄分布
age_bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
data['Age'] = pd.cut(data['Age'], bins=age_bins, labels=age_bins[1:], include_lowest=True)
age_distribution = data['Age'].value_counts()

# 创建条形图
sns.barplot(x=age_distribution.index, y=age_distribution.values, palette='viridis')
plt.title('Age Distribution')
plt.xlabel('Age Group')
plt.ylabel('Number of Passengers')
plt.savefig("Titanic(4).png")
plt.show()

# 分析SibSp（同船配偶或兄弟姐妹的数量）对生还率的影响
sibsp_survival = data.groupby('SibSp')['Survived'].mean()
sibsp_survival = sibsp_survival.sort_index()

# 创建条形图
sns.barplot(x=sibsp_survival.index, y=sibsp_survival.values, palette='viridis')
plt.title('Survival Rate by SibSp')
plt.xlabel('SibSp')
plt.ylabel('Survival Rate')
plt.savefig("Titanic(5).png")
plt.show()

# 分析Parch（同船父母或子女的数量）对生还率的影响
parch_survival = data.groupby('Parch')['Survived'].mean()
parch_survival = parch_survival.sort_index()

# 创建条形图
sns.barplot(x=parch_survival.index, y=parch_survival.values, palette='viridis')
plt.title('Survival Rate by Parch')
plt.xlabel('Parch')
plt.ylabel('Survival Rate')
plt.savefig("Titanic(6).png")
plt.show()

# 分析Fare（票价）对生还率的影响，将Fare分为若干区间
fare_bins = [0, 20, 40, 60, 80, 100, 200, 300, 400, 500]
data['Fare_Group'] = pd.cut(data['Fare'], bins=fare_bins, labels=fare_bins[1:], include_lowest=True)
fare_survival = data.groupby('Fare_Group')['Survived'].mean()

# 创建条形图
sns.barplot(x=fare_survival.index, y=fare_survival.values, palette='viridis')
plt.title('Survival Rate by Fare')
plt.xlabel('Fare Group')
plt.ylabel('Survival Rate')
plt.savefig("Titanic(7).png")
plt.show()

# 分析Cabin（船舱号）对生还率的影响
# 对于'Cabin'缺失值，将有无船舱号作为一个特征
data['Cabin'] = data['Cabin'].fillna('No Cabin')
data['HasCabin'] = data['Cabin'].apply(lambda x: 0 if x == 'No Cabin' else 1)
cabin_survival = data.groupby('HasCabin')['Survived'].mean()

# 创建条形图
sns.barplot(x=cabin_survival.index, y=cabin_survival.values, palette='viridis')
plt.title('Survival Rate by Cabin Availability')
plt.xlabel('Has Cabin')
plt.ylabel('Survival Rate')
plt.savefig("Titanic(8).png")
plt.show()
