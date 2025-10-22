class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.nums_og = nums[:]
        

    def reset(self) -> List[int]:
        return self.nums_og
        

    def shuffle(self) -> List[int]:
        n = len(self.nums)
        for i in range(n - 1, 0, -1):
                j = random.randint(0, i)  # pick a random index from 0..i
                self.nums[i], self.nums[j] = self.nums[j], self.nums[i]  # swap
        return self.nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()