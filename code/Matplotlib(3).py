import pandas as pd

# 创建一个包含学生信息的数据集
data = {'班级': ['A', 'B', 'A', 'B', 'A', 'B'],
        '学生姓名': ['张三', '李四', '王五', '赵六', '钱七', '孙八'],
        '分数': [85, 90, 88, 92, 78, 95]}

df = pd.DataFrame(data)

# 使用 groupby 函数按照班级进行分组
grouped_df = df.groupby('班级')

# 计算每个班级的平均分数
average_scores = grouped_df['分数'].mean()

# 打印结果
print(grouped_df)
print(average_scores)

