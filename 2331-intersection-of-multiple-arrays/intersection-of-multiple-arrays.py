class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        f=set(nums[0])

        for i in nums[1:]:
            f=f.intersection(i)

        a=list(f)
        a.sort()
        return a
                
