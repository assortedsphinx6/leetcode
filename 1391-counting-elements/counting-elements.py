class Solution:
    def countElements(self, arr: List[int]) -> int:
        hashset = set(arr)
        ans = 0
        
        for i in range(len(arr)):
            if arr[i] + 1 in hashset:
                ans += 1
        
        return ans