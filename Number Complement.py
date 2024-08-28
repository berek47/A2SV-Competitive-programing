class Solution:
    def findComplement(self, num: int) -> int:
        complement: int = 0  
        power: int = 1 

        while num > 0:
            current_bit: int = num & 1  
            if current_bit == 0:
                complement += power

            power <<= 1
            num >>= 1
        return complement
