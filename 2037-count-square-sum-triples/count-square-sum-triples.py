import numpy as np
class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        for i in range(1,n):
            for j in range(1,n):
                if ((i**2) + (j**2)) <= (n**2) and i!=j and np.sqrt((i**2) + (j**2)).is_integer():
                    count=count+1
        return count