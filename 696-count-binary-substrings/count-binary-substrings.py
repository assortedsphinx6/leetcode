class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans, prev, curr = 0, 0, 1
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                ans += min(prev, curr)
                prev = curr
                curr = 1
            else:
                curr += 1
        ans += min(prev, curr)
        return ans