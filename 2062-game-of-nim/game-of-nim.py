class Solution:
    def nimGame(self, piles: List[int]) -> bool:
        return bool(reduce(operator.xor, piles))