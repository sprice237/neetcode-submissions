class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a = 0
        s = 0

        for n in nums:
            a += 1
            s -= n

        s += a * (a + 1) // 2

        return s
        