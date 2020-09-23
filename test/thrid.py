import numpy as np

# 创建一个一维数组
names = np.array(['James','Bob','Teresa','Bob'])
# 使用np.unique函数找出元素为一值并排序（去重排序）
print(np.unique(names))

# 查询names数组中是否存在指定列表元素
print(np.in1d(names, ['James','Bob']))


# #创建一个数正态分布的一维数组
# arr = np.random.randn(10)
# # 将数组数据写入到文件中
# np.save('my_array', arr)
# print('Save data is successfully!')
# # 读取二进制文件
# print(np.load('my_array.npy'))


# 创建一个2行3列的二维数组矩阵
arr1 = np.arange(2,6).reshape((2,2))
print(arr1)
# 创建一个3行3列的二维数组矩阵
arr2 = np.arange(6,10).reshape((2,2))
print(arr2)
# arr1数组矩阵乘以arr2数组矩阵
print(arr1.dot(arr2)) # 等价np.dot(arr1,arr2)
# 二维矩阵与一维矩阵点积运算后得到一个一维数组
print(np.dot(arr1, np.ones(2)))



# 导入NumPy模块
import numpy as np
# 导入linalg
from numpy.linalg import inv, qr
# 创建一个5*5的正态分布二维数组矩阵
arr = np.random.randn(3,3)
print(arr)
# 获取矩阵的逆运算值
print(inv(arr))
# 获取矩阵的QR分解操作值
q,r = qr(arr)
print(r)

from pandas import Series

obj = Series([2,1,7,-4,9])
print(obj)


# 创建SeriesA
dictA = {'Ohio':35000, 'Oregon':16000, 'Texas':71000, 'Utah':5000}
seriesA = Series(dictA)

# 创建SeriesB
new_index = {'California', 'Ohio', 'Oregon', 'Texas'}
seriesB = Series(dictA, new_index)

# seriesA和seriesB自动对齐
print(seriesA + seriesB)





