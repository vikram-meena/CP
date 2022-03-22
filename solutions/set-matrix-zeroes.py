# Objective: Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
# Observation: 
#   1. While performing inplace operations use first row and columns for memory usages
#   2. Modify array from other end 
  
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #
        row = len(matrix)
        column = len(matrix[0])
        r_0 =1
        # Track all rows and columns with zeros
        for i in range(row):
            for j in range(column):
                if not matrix[i][j]:
                    if i == 0: 
                        r_0 = 0 
                    else: 
                        matrix[i][0] = 0
                        matrix[0][j] = 0 
        # start filling with zeros from last row and columns based on first row and columns
        for i in range(row - 1, 0, -1):
            for j in range(column - 1, -1, -1): 
                if matrix[i][0]  == 0 or matrix[0][j] == 0: 
                    matrix[i][j] = 0
        if not r_0:
            for j in range(column - 1, -1, -1): 
                matrix[0][j] = 0

# Use Cases:
# Image Manipulation
