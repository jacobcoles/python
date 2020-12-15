import numpy

input_list = [[1,2,3], [1,2,3,4,5], [1,2], [1,2,3,4,5,6,7,8]]

def pad(input_list):
	"""
	Given a input list of nested list of integers:

	input_list = [[1,2,3], [1,2,3,4,5], [1,2], [1,2,3,4,5,6,7,8]]

	return a matrix where 
	1) matrix[i][:len(input_list[i])] == input_list[i]
	and
	2) matrix[i][len(input_list[i]):] == [0,0, ..., 0]

	"""
	#pass
	
	#from the bottom item of 'matrix' up to the length of 'input' item 'i', will be the same as item 'i' in 'input'
	
	#numpy.pad(input_list)
	
	max_length = len(max(input_list, key=len))
	
	matrix = []
	for item in input_list:
		extra_zeroes = max_length - len(item)
		matrix.append(list(numpy.pad(item, (0,extra_zeroes), 'constant')))
	
	return matrix
		
print(pad(input_list))
