import array as arr
import numpy
import sys

# Use array package
x = arr.array("i", [1, 2, 3, 4, 5])
print(x)
print(type(x))

# Or using list
y = [1, 2, 3, 4, 5]
print(y)

# 2 Dimension Array
y = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(y)
print(y[0][1])

# 2 Dimeonsion Array using numpy
z = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(z)
print(z[0][1])

# Memory Size
print("List Memory Size: ", sys.getsizeof(y) * len(y), "bytes")
print("NumPy Memory Size: ", z.size * z.itemsize, "bytes")

# Matrix Declaration with Default Value
# a = [[0] * 3 for i in range(3)]
a = [[0 for j in range(3)] for i in range(3)]
print(a)
