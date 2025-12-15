from typing import List
import heapq

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:

        def gain(p, t):
            return (p + 1) / (t + 1) - p / t

        # max heap using negative gain
        heap = []
        for p, t in classes:
            heapq.heappush(heap, (-gain(p, t), p, t))

        # assign extra students
        for _ in range(extraStudents):
            _, p, t = heapq.heappop(heap)
            p += 1
            t += 1
            heapq.heappush(heap, (-gain(p, t), p, t))

        # compute final average
        total = 0
        for _, p, t in heap:
            total += p / t

        return total / len(classes)