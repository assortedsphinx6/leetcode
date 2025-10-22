class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        dp = [0] * len(energy)
        for i in range(len(dp)-1,-1,-1):
            if i + k < len(dp):
                dp[i] = dp[i+k] + energy[i]
            else:
                dp[i] = energy[i]
        return max(dp)