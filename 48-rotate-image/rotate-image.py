class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # transpose
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        transposed = [list(row) for row in zip(*matrix)]
        for i in range(len(matrix)):
            matrix[i][:] = transposed[i][::-1]   # overwrite each row with reversed version
