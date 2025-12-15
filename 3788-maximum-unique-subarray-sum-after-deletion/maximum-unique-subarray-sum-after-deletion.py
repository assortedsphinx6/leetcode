class Solution:
    def maxSum(self, nums: List[int]) -> int:
        res = 0 # return this if following resulting array is empty
        s = set(nums)
        for item in s:
            if item > 0:
                res += item
        if res == 0:
            return max(s)
        else:
            return res