class Solution:
    def minTimeToType(self, word: str) -> int:
        count = 0
        curr = "a"
        for ch in word:
            diff = abs(ord(ch) - ord(curr))
            step = min(diff, 26-diff)
            count += step + 1
            curr = ch

        return count