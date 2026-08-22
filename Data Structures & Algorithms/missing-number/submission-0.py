class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a = len(nums)
        s = a * (a + 1) // 2

        for n in nums:
            s -= n

        return s
        