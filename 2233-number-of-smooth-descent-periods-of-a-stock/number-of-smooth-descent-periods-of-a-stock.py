class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        j = 1
        i = 0
        cnt = 1
        res = 0
        while j<len(prices): 
            if prices[j-1] - prices[j] == 1:
                cnt += 1
            else:
                res += cnt * (cnt + 1) // 2
                cnt = 1
            j += 1
        res += cnt * (cnt + 1) // 2
        return res





        