class Solution:
    def minTimeToType(self, word: str) -> int:
        time = 0
        curr = 'a'
        for ch in word:
            diff = abs(ord(ch) - ord(curr))
            time += min(diff, 26 - diff) + 1
            curr = ch
        return time
