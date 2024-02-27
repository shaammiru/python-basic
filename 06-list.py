# List is a collection which is ordered and changeable. Allows duplicate members.
my_list = [1, "Hello", True, 1.0]
my_list[0] = 2
print(my_list)
print(my_list[1])
print(my_list[-2])

# Slicing and Sequence
# [start:stop:step]
print(my_list[0:3:2])
# [start:]
print(my_list[1:])
# [:stop]
print(my_list[:3])

# List Methods
print(len(my_list))
print(min([1, 2, 3]))
print(max([1, 2, 3]))
print(sum([1, 2, 3]))
print(my_list.count(1))

# In and Not In
print(1 in my_list)
print(1 not in my_list)

