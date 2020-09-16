import numpy as np
import matplotlib.pyplot as plt

arr = np.empty((5, 4), dtype=np.int);
for i in range(5):
    arr[i] = i
print(arr)

arr = np.arange(21).reshape((3, 7))
print(arr)

arr = np.arange(27).reshape((3, 3, 3))
print(arr)

print('------------')
arr = np.arange(32).reshape((8, 4))
print(arr)
print(arr[[1, 5, 7, 2], [0, 3, 1, 2]])
print(arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]])

print(arr.T)

arr = np.arange(24).reshape(2, 3, 4)
print(arr)
print(arr.transpose(1, 0, 2))

arr = np.arange(10)
print(arr)
print(np.sqrt(arr))

print()
arr = np.arange(0, 1, 0.1)
print(arr)
rx, ry = np.meshgrid(arr, arr)
print(rx, ry)
data = np.sqrt(np.square(rx) + np.square(ry))
print(data)

# # 设置图表的样式
# plt.imshow(data)#, cmap=plt.cm.black
# # 设置右侧图例条
# plt.colorbar()
# # 设置图表标题
# plt.title('Image plot of sqrt(square(xs)+square(ys) for agrid values')
# plt.show() # 显示


flag = np.array([True, False, True, False, True])
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])
result = [(x if z else y) for x, y, z in zip(arr1, arr2, flag)]
print(result)


arr = np.random.randn(4, 4)
print(arr)
arr1 = np.where(arr > 0, 2, -2)
print(arr1)
arr = np.where(arr > 0, 2, arr)
print(arr)
