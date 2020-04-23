import numpy as np

# 结构数组
persontype = np.dtype({
    'names': ['name', 'age', 'chinese', 'math', 'english'],
    'formats': ['S1', 'i', 'i', 'i', 'f']
})

peoples = np.array([
    ("ZhangFei", 32, 75, 100, 90),
    ("GuanYu", 24, 85, 96, 88.5),
    ("ZhaoYun", 28, 85, 92, 96.5),
    ("HuangZhong", 29, 65, 85, 100)
], dtype=persontype)

ages = peoples[:]['age']
chinese = peoples[:]['chinese']
math = peoples[:]['math']
english = peoples[:]['english']

print(np.mean(ages))
print(np.mean(chinese))
print(np.mean(math))
print(np.mean(english))

print(np.max(ages))
print(math)

# ufunc运算
# 算数运算
x1 = np.arange(1, 11, 2)
x2 = np.linspace(1, 9, 5)

print(np.add(x1, x2))
print(np.subtract(x1, x2))
print(np.multiply(x1, x2))
print(np.divide(x1, x2))
print(np.power(x1, x2))
print(np.remainder(x1, x2))

# 统计函数

# 计数组 / 矩阵中的最大值函数 amax()，最小值函数 amin()
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(np.amin(a))
print(np.amin(a, 0))
print(np.amin(a, 1))

print(np.amax(a))
print(np.amax(a, 0))
print(np.amax(a, 1))

# 统计最大值与最小值之差
print(np.ptp(a))
print(np.ptp(a, 0))
print(np.ptp(a, 1))

# 百分位数
print(np.percentile(a, 50))
print(np.percentile(a, 50, axis=0))
print(np.percentile(a, 50))

# 中位数
print(np.median(a))
print(np.median(a, axis=0))
print(np.median(a, axis=1))

# 平均数
print(np.mean(a))
print(np.mean(a, axis=0))
print(np.mean(a, axis=1))

# 统计数组中的加权平均值 average()
a = np.array([1, 2, 3, 4])
wts = np.array([1, 2, 3, 4])
print(np.average(a))
print(np.average(a, weights=wts))

