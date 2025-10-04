"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        ans = []
        x_i, x_j = 1, 1000

        while x_i <= x_j:
            y_i, y_j = 1, 1000
            while y_i <= y_j:
                mid = (y_i + y_j)//2
                val = customfunction.f(x_i, mid)
                if val == z:
                    ans.append([x_i, mid])
                    break
                if val < z :
                    y_i = mid + 1
                else:
                    y_j = mid - 1
                
            x_i += 1
        return ans
                    