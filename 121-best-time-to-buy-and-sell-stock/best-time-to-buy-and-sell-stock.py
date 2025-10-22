class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        min_seen: float = math.inf
        max_profit: int = 0

        for price in prices:
            if price < min_seen:
                min_seen = price
            elif price - min_seen > max_profit:
                max_profit = price - min_seen
        
        return max_profit
        

            

        