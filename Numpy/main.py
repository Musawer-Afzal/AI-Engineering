import numpy as np

# my_list = [1, 2, 3, 4]
# my_list = my_list * 2
# print(my_list)

# A numpy is superior
# array = np.array([1, 2, 3, 4])
# array = array * 2
# print(array)

# Multi dimensional Array/Indexing
array = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                  [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
                  [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', ' ']]])
print(array.shape)
print(array[0, 1, 0])

word = array[0, 0, 0]
print(word) 