class Solution:
    def countLetters(self, s: str) -> int:
        total = 0
        streak = 0
        for i in range(len(s)):
            if i==0 or s[i] == s[i-1]:
                streak += 1
            else:
                streak = 1
        
            total += streak
        return total