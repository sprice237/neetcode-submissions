class Solution:
    def reverseBits(self, n: int) -> int:
        x = 0
        b = 32

        while n > 0:
            b -= 1
            i = n & 1
            n = n >> 1
            x = x << 1
            x = x | i

        x = x << b

        return x