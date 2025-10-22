class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        if len(sticks) == 1:
            return 0
        sticks.sort()
        x, y = sticks[0], sticks[1]
        merged = x + y
        return merged + self.connectSticks([merged] + sticks[2:])
