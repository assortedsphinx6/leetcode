class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        d = {}
        for arr in nums:
            for x in arr:
                d[x] = d.get(x,0) + 1
        res = []
        for key in d:
            if d[key] == len(nums):
                res.append(key)
        return sorted(res)
                
