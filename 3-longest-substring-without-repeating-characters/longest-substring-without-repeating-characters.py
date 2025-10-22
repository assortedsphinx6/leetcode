class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = [-1] * 128
        left = 0
        best = 0

        for i, ch in enumerate(s):
            j = ord(ch)
            if last[j] >= left:
                left = last[j] + 1
            last[j] = i
            cur = i - left + 1
            if cur > best:
                best = cur
        return best