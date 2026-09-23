class Solution:
    def luckyNumbers(self, matrix: list[list[int]]) -> list[int]:
        min_val = []
        max_cols = []

        # minimum value in each row
        for row in matrix:
            min_val.append(min(row))

        # maximum value in each column
        for col in range(len(matrix[0])):
            curr_col = []

            for row in range(len(matrix)):
                curr_col.append(matrix[row][col])

            max_cols.append(max(curr_col))

        # lucky numbers appear in both
        result = []

        for item in min_val:
            if item in max_cols:
                result.append(item)

        return result