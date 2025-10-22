import heapq
from typing import List

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        if len(sticks) <= 1:
            return 0

        heapq.heapify(sticks)  # turn into min-heap
        cost = 0

        while len(sticks) > 1:
            x = heapq.heappop(sticks)
            y = heapq.heappop(sticks)
            new = x + y
            cost += new
            heapq.heappush(sticks, new)

        return cost
