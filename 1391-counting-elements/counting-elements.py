class Solution:
    def countElements(self, arr: List[int]) -> int:
        counter = Counter(arr)
        return sum(v for k,v in counter.items() if k+1 in counter)