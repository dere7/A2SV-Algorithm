from typing import List

class Solution:
	def __init__(self, matrix: List[List[int]]):
		self.matrix = matrix
		self.suff_matrix = matrix
		
		for i in range(len(matrix)):
			for j in range(1,len(matrix[0])):
				self.suff_matrix[i][j] += self.suff_matrix[i][j-1]
				
	def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
		i, j = row1, col1
		sums = 0
		while i <= row2:
			if col1 -1  >= 0:
				sums += (self.suff_matrix[i][col2] - self.suff_matrix[i][col1-1])
			else:
				sums += self.suff_matrix[i][col2]
			i += 1
		return sums