from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if k <= 0 or n == 0:
            return []
        if k == 1:
            return nums[:]  # trivial fast path

        dq = deque()              # stores indices; nums[dq] is decreasing
        out= []
        a = nums                  # local binding (micro-opt)

        for i, x in enumerate(a):
            # pop smaller/equal elements (they can't be max with x in window)
            while dq and a[dq[-1]] <= x:
                dq.pop()
            dq.append(i)

            # remove indices that are out of the current window [i-k+1, i]
            if dq[0] <= i - k:
                dq.popleft()

            # record max when window has k elements
            if i >= k - 1:
                out.append(a[dq[0]])

        return out
