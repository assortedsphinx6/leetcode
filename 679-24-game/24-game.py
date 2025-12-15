from typing import List

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        EPS = 1e-6

        def dfs(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < EPS

            n = len(nums)
            for i in range(n):
                for j in range(n):
                    if i == j:
                        continue

                    a, b = nums[i], nums[j]
                    next_nums = []

                    # keep remaining numbers
                    for k in range(n):
                        if k != i and k != j:
                            next_nums.append(nums[k])

                    # addition (commutative)
                    if i < j:
                        next_nums.append(a + b)
                        if dfs(next_nums):
                            return True
                        next_nums.pop()

                    # multiplication (commutative)
                    if i < j:
                        next_nums.append(a * b)
                        if dfs(next_nums):
                            return True
                        next_nums.pop()

                    # subtraction
                    next_nums.append(a - b)
                    if dfs(next_nums):
                        return True
                    next_nums.pop()

                    # division
                    if abs(b) > EPS:
                        next_nums.append(a / b)
                        if dfs(next_nums):
                            return True
                        next_nums.pop()

            return False

        return dfs([float(c) for c in cards])