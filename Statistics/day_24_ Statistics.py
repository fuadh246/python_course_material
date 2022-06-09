# How to import numpy
import numpy as np
# How to check the version of the numpy package
print('numpy:', np.__version__)
# Checking the available methods
#print(dir(np))

# Creating numpy array using

python_list = [1,2,3,4,5]
# Checking data types
print('Type:', type (python_list)) # <class 'list'>
print(python_list) # [1, 2, 3, 4, 5]
two_dimensional_list = [[0,1,2], [3,4,5], [6,7,8]]
print(two_dimensional_list)  # [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
# Creating Numpy(Numerical Python) array from python list
numpy_array_from_list = np.array(python_list)
print(type (numpy_array_from_list))   # <class 'numpy.ndarray'>
print(numpy_array_from_list) # array([1, 2, 3, 4, 5])


# Creating a float numpy array from list with a float data type parameter

python_list = [1,2,3,4,5,6]
numpy_array_from_list2 = np.array(python_list,dtype=float)
print(numpy_array_from_list2)

# Creating boolean numpy arrays
numpy_bool_array = np.array([0, 1, -1, 0, 0], dtype=bool)
print(numpy_bool_array) # array([False,  True,  True, False, False])

# Creating multidimensional array using numpy

two_dimensional_list = [[0,1,2], [3,4,5], [6,7,8]]
numpy_two_dimensional_list = np.array(two_dimensional_list)
print('numpy_two_dimensional_list: ')
print(numpy_two_dimensional_list)

# Converting numpy array to list
# We can always convert an array back to a python list using tolist().

np_to_list = numpy_array_from_list.tolist()
print(type(np_to_list))
print((np_to_list))

# Shape of numpy array
'''
The shape method provide the shape of the array as a tuple. The 
first is the row and the second is the column. If the array is just 
one dimensional it returns the size of the array.
'''
nums = np.array([1, 2, 3, 4, 5])
print(nums)
print('Shape of nums: ',nums.shape)
print(numpy_two_dimensional_list)
print('shape of numpy_two_dimensional_list: ', numpy_two_dimensional_list.shape)
three_by_four_array = np.array([[0, 1, 2, 3],
        [4,5,6,7],
        [8,9,10, 11]])
print('shape of numpy_two_dimensional_list: ', three_by_four_array.shape)

print()
print()
print()
int_lists = [-3, -2, -1, 0, 1, 2,3]
int_array = np.array(int_lists)
float_array = np.array(int_lists, dtype=float)

print(int_array)
print(int_array.dtype)
print(float_array)
print(float_array.dtype)

print()
print()
print()

numpy_array_from_list = np.array([1, 2, 3, 4, 5])
two_dimensional_list = np.array([[0, 1, 2],
                              [3, 4, 5],
                              [6, 7, 8]])

print('The size:', numpy_array_from_list.size) # 5
print('The size:', two_dimensional_list.size)  # 3

print()
print()
print()

two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
first_row = two_dimension_array[0]
second_row = two_dimension_array[1]
third_row = two_dimension_array[2]
print(two_dimension_array)
print('First row:', first_row)
print('Second row:', second_row)
print('Third row: ', third_row)

print()
first_column= two_dimension_array[:,0]
second_column = two_dimension_array[:,1]
third_column = two_dimension_array[:,2]
print('First column:', first_column)
print('Second column:', second_column)
print('Third column: ', third_column)