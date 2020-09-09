import numpy as np

data1 = [[1,2,3,4,5],[6,7,8,'a',0]]
#创建数组
data2 = np.array(data1)
#打印数组
print(data2)
#输出数组大小
print(data2.shape)
#数组的类型
print(data2.dtype)
print()

#创建数组的其他方法
arr1 = np.zeros(5)
arr2 = np.ones((2,3))
arr3 = np.empty((2,3,4))
arr4 = np.arange(5)
arr5 = np.array([[1,2,3,4], np.arange(5,9)])

print(arr1)
print(arr2)
print(arr3)
print(arr4)
print(arr5)


