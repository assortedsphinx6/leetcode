from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        c_s = Counter(s)
        c_t = Counter(t)
        sorted_t = "".join(sorted(t))
        sorted_s = "".join(sorted(s))
        count = sum((c_t - c_s).values())
        return count
        count = len(set("practice") - set("leetcode")) # characters in t but not in s need to be added
        
        # must account for characters that exist in both s and t but in diff numbers