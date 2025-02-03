import numpy as np

print(np.__version__)

arr = np.array([1, 2, 3, 4, 5])
print(type(arr))
print(arr[3])
print(arr[0] + arr[2]) 


print(arr)

arr1 = np.array([1, 2, 3, 4, 5, "jasdk"], dtype="S")
print(arr1)
print(arr1[0:3])
print(arr1.dtype) 


arr2 = np.array([[[1, 2, 3], [4, 5, 6]],[[4,6,7],[8,3,2]],[[1, 2, 3], [4, 5, 6]]])
print("2nd element from every line",arr2[0:1, 1])
print(arr2.dtype) 
print(arr2)

arr3 = np.array([[1,2,546,4,5], [6,123,8,9,10]],dtype="i")
print("3rd element line 1",arr3[0,2])
print(arr3[0,-1])

print(np.__version__)

