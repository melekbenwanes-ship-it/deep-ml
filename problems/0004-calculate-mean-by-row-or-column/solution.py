import numpy as np
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	matrix=np.array(matrix)
	means=[]
	s=0
	if mode=='column':
		means=matrix.sum(axis=0)/matrix.shape[0]
	
	elif mode=='row':
		means=matrix.sum(axis=1)/matrix.shape[1]
	return means