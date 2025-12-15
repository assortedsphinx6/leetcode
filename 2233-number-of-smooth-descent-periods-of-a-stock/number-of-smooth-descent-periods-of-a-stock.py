class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        res = 0
        cnt = 1

        for i in range(1, len(prices)):
            if prices[i - 1] - prices[i] == 1:
                cnt += 1
            else:
                res += cnt * (cnt + 1) // 2
                cnt = 1

        res += cnt * (cnt + 1) // 2
        return res