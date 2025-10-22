class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeros = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zeros.append([i,j])

        for zero in zeros:
            matrix[zero[0]] = [0] * len(matrix[0])
            for i in range(len(matrix)):
                matrix[i][zero[1]] = 0      