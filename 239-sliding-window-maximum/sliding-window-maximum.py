from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k <= 0: 
            return []
        n = len(nums)
        if k > n:
            return [max(nums)] if nums else []
        
        dq = deque()  # stores indices; nums[dq] is decreasing
        out: List[int] = []

        for i, x in enumerate(nums):
            # Remove smaller/equal elements from the back
            while dq and nums[dq[-1]] <= x:
                dq.pop()
            dq.append(i)

            # Remove front if it's out of window
            if dq[0] <= i - k:
                dq.popleft()

            # Record max when window is formed
            if i >= k - 1:
                out.append(nums[dq[0]])
        return out
