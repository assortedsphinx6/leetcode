from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        freq = [0] * 26
        for a, b in zip(s, t):
            freq[ord(a) - 97] += 1
            freq[ord(b) - 97] -= 1
        return sum(x for x in freq if x > 0)
       
