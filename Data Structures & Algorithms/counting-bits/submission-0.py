class Solution:
    def countBits(self, n: int) -> List[int]:
        def count_bits_in_number(n: int):
            c = 0

            while n > 0:
                if n % 2 == 1:
                    c += 1
                n = n // 2

            return c

        return [count_bits_in_number(x) for x in range(n + 1)]

        