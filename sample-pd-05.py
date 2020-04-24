from pandas import Series, DataFrame

x1 = Series([1, 2, 3, 4])
x2 = Series(data=[1, 2, 3, 4], index=['a', 'b', 'c', 'd'])

print(x1)
print(x2)

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
x3 = Series(d)
print(x3)

data = {'Chinese': [66, 95, 93, 90, 80], 'English': [65, 85, 92, 88, 90], 'Math': [30, 98, 78, 34, 64]}
df1 = DataFrame(data)
df2 = DataFrame(data, index=['zhangfei', 'guanYu', 'ZhaoYun', 'Huangzhong', 'DianWei'])

# df2 = df2.drop(columns=['Chinese'])
# df2 = df2.drop(index=['zhangfei'])
df2 = df2.drop_duplicates()

print(df1)
print(df2)
