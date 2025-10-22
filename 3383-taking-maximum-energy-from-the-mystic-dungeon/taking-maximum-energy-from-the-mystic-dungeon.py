class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:

        dp = [0] * (len(energy) + k) # let dp[i] note the energy we gain starting from index i

        # dp[i] = dp[i+k] + energy[i]
        for i in range(len(energy)-1,-1,-1):
            dp[i] = energy[i] + dp[i+k]

        print (dp)
        return max(dp[:len(energy)])
