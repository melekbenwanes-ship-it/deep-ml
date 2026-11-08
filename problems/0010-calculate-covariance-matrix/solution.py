import numpy as np
def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	v=np.array(vectors)
	m=np.cov(v)
	return m.tolist()