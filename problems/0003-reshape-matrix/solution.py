import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	a=np.array(a)
	if (a.shape[0]== new_shape[1] or a.shape[1]== new_shape[0] or (a.shape[1]== new_shape[1] and a.shape[0]== new_shape[0])): 
		reshaped_matrix=a.reshape(new_shape[0],new_shape[1])
	else:
		reshaped_matrix=[]
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	return reshaped_matrix