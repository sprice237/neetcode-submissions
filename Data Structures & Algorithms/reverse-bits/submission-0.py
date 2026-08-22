class Solution:
    def reverseBits(self, n: int) -> int:
        x = 0

        for _ in range(32):
            i = n & 1
            n = n >> 1
            x = x << 1
            x = x | i

        return x