from math import isqrt
class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        for a in range(1,n+1):
            aa = a*a
            for b in range(a+1, n+1): # ensure a<b
                s = aa + b*b
                c = isqrt(s)
                if c<=n and c*c == s:
                    count += 1
        return count * 2

# a can never equal b since a^2 + a^2 = 2a^2, therefore c = a*root(2) which is irrational
