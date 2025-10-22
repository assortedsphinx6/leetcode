class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:

        dp = [0] * len(energy) # let dp[i] note the energy we gain starting from index i

        # dp[i] = dp[i+k] + energy[i]
        for i in range(len(dp)-1,-1,-1):
            if i+k < len(dp):
                dp[i] = energy[i] + dp[i+k]
            else:
                dp[i] = energy[i]

        return max(dp)
