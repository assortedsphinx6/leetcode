class Solution:
    def findComplement(self, num: int) -> int:
        # create a mask with all 1's covering the bits of num
        mask = (1 << num.bit_length()) - 1
        return num ^ mask
        