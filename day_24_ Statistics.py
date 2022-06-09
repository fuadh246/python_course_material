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

# Slicing Numpy array
print('Slicing Numpy array')
two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
first_two_rows_and_columns = two_dimension_array[0:2, 0:2]
print(first_two_rows_and_columns)


print()
print()
print('Reverse the row and column positions: ')
two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
two_dimension_array[::-1,::-1]
print(two_dimension_array[::-1,::-1])

print()
print()
numpy_zeroes = np.zeros((3,3),dtype=int,order='C')
print(numpy_zeroes)
print()
print()
numpy_ones = np.ones((3,3),dtype=int,order='C')
print(numpy_ones)

# Reshape
# numpy.reshape(), numpy.flatten()
first_shape  = np.array([(1,2,3), (4,5,6)])
print(first_shape)
print()
reshaped = first_shape.reshape(3,2)
print(reshaped)


flattened = reshaped.flatten()
print(flattened)

array = np.array([[[1,2],[3,4]]])
flattened = array.flatten()
print(flattened)

print()
print()
np_list_one = np.array([1,2,3])
np_list_two = np.array([4,5,6])
print(np_list_one + np_list_two)
print('Horizontal Append:', np.hstack((np_list_one, np_list_two)))
print('Vertical Append:',np.vstack((np_list_one,np_list_two)))

print()
print()

random_float = np.random.random()
print('random: ',random_float)

random_float = np.random.random(5)
print('random 5 float: ',random_float)

random_int = np.random.randint(0,11)
print('random number between 0 to 10: ',random_int)

random_int = np.random.randint(0,11, size=4)
print('random 4 numbers between 2 to 10: ',random_int)

random_int = np.random.randint(0,11, size=(4,4))
print('random 4 by 4 numbers between 2 to 10: \n',random_int)

normal_array = np.random.normal(79, 15, 80)
#print(normal_array)

# Numpy and Statistics

import matplotlib.pyplot as plt
import seaborn as sns
# sns.set()
# plt.hist(normal_array, color="grey", bins=50)
# plt.show()

# Numpy numpy.arange()
lst = np.arange(0, 11, 2)
print(lst)
# Creating sequence of numbers using linspace
list=np.linspace(1.0, 5.0, num=5, endpoint=False)
print(list)
# LogSpace
# LogSpace returns even spaced numbers on a log scale. Logspace has the same parameters as np.linspace.
# Syntax:
# numpy.logspace(start, stop, num, endpoint)
list = np.logspace(2, 3.0, num=4)
print(list)

'''
Numpy Functions
Min np.min()
Max np.max()
Mean np.mean()
Median np.median()
Varience
Percentile
Standard deviation np.std()'''
print()
print()
print()
print()
np_normal_dis = np.random.normal(5, 0.5, 100)
np_normal_dis
## min, max, mean, median, sd
print('min: ', two_dimension_array.min())
print('max: ', two_dimension_array.max())
print('mean: ',two_dimension_array.mean())
# print('median: ', two_dimension_array.median())
print('sd: ', two_dimension_array.std())
print()
print()
print(two_dimension_array)
print('Column with minimum: ', np.amin(two_dimension_array,axis=0))
print('Column with maximum: ', np.amax(two_dimension_array,axis=0))
print('=== Row ==')
print('Row with minimum: ', np.amin(two_dimension_array,axis=1))
print('Row with maximum: ', np.amax(two_dimension_array,axis=1))

print(np.random.choice(['a', 'e', 'i', 'o', 'u'], size=10))

from scipy import stats
np_normal_dis = np.random.normal(5, 0.5, 1000) # mean, standard deviation, number of samples
np_normal_dis
## min, max, mean, median, sd
print('min: ', np.min(np_normal_dis))
print('max: ', np.max(np_normal_dis))
print('mean: ', np.mean(np_normal_dis))
print('median: ', np.median(np_normal_dis))
print('mode: ', stats.mode(np_normal_dis))
print('sd: ', np.std(np_normal_dis))

#plt.hist(np_normal_dis, color="black", bins=21)
#plt.show()

# Linear Algebra
# Dot Product
## Linear algebra
### Dot product: product of two arrays
f = np.array([1,2,3])
g = np.array([4,5,3])
### 1*4+2*5 + 3*6
print(np.dot(f, g)) # 23

# NumPy Matrix Multiplication with np.matmul()
h = [[1,2],[3,4]]
i = [[5,6],[7,8]]
### 1*5+2*7 = 19
print(np.matmul(h, i))


temp = np.array([1,2,3,4,5])
pressure = temp * 2 + 5
print(pressure)
# plt.plot(temp,pressure)
# plt.xlabel('Temperature in oC')
# plt.ylabel('Pressure in atm')
# plt.title('Temperature vs Pressure')
# plt.xticks(np.arange(0, 6, step=0.5))
# plt.show()

# plt.plot(pressure,temp)
# plt.xlabel('Temperature in oC')
# plt.ylabel('Pressure in atm')
# plt.title('Temperature vs Pressure')
# plt.xticks(np.arange(0, 17, step=1))
# plt.show()

mu = 28
sigma = 15
samples = 100000

# x = np.random.normal(mu, sigma, samples)
# ax = sns.distplot(x);
# ax.set(xlabel="x", ylabel='y')
# plt.show()