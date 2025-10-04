class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: # negative numbers cannot be palindromes
            return False 
            print("neg")
        
        if x%10 == 0 and x!=0: # numbers ending with 0 but not 0 itself cannot be palindromes
            return False
            print("num ending in 0")

        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        # for odd digit counts, remove the middle digit (reversed_half // 10) - integer quotient
        return x == reversed_half or x == reversed_half // 10