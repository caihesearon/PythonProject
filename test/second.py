import numpy as np


arr = np.empty((5,4), dtype=np.int);
for i in range(5):
    arr[i] = i
print(arr)


arr = np.arange(21).reshape((3,7))
print(arr)

arr = np.arange(27).reshape((3,3,3))
print(arr)

print('------------')
arr = np.arange(32).reshape((8,4))
print(arr)
print(arr[[1,5,7,2],[0,3,1,2]])
print(arr[[1,5,7,2]][:,[0,3,1,2]])