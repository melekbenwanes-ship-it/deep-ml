import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	A=np.array(A)
	S=np.array(S)
	T=np.array(T)
	if (np.linalg.det(S)!=0 and np.linalg.det(T)!=0):	
		P=np.linalg.inv(T)
		transformed_matrix=P@A@S
	else:
		return [[-1]]
	

	
	return transformed_matrix.tolist()