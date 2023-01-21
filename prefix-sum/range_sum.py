import pprint
class NumMatrix:
	def __init__(self, matrix):
		n = len(matrix)
		m = len(matrix[0])
		prefix_sum = [[0] * m] * n
		for i in range(n):
			for j in range(m):
				if i == 0 and j == 0:
					prefix_sum[i][j] = matrix[i][j]
				elif i == 0 and j > 0:
					prefix_sum[i][j] = prefix_sum[i][j - 1] + matrix[i][j]
				elif i > 0 and j == 0:
					prefix_sum[i][j] = prefix_sum[i - 1][j] + matrix[i][j]
				else:
					prefix_sum[i][j] = prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1] + matrix[i][j]
					
		pprint.pprint(prefix_sum)

matrix = [
	[3, 0, 1, 4, 2], 
	[5, 6, 3, 2, 1], 
	[1, 2, 0, 1, 5], 
	[4, 1, 0, 1, 7], 
	[1, 0, 3, 0, 5]
]
obj = NumMatrix(matrix)
