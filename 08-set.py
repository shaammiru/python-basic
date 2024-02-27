# Set is a collection of unique elements, can't be accessed by index
my_set = {1, 2, 3}
other_set = {3, 4, 5}
print(my_set)

union = my_set.union(other_set)
print(union)
intersection = my_set.intersection(other_set)
print(intersection)