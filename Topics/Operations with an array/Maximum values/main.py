import numpy as np

num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

arr = np.array([num_1, num_2, num_3])

print(arr.max(axis=0))
print(arr.argmax())


