class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total = sum(nums)
        pref = 0
        ans = 0
        # i goes only to n-2 so right side stays non-empty
        for i in range(len(nums) - 1):
            pref += nums[i]
            if pref >= total - pref:
                ans += 1
        return ans
