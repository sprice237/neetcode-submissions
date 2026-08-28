class Solution:
    def rob(self, nums: List[int]) -> int:
        num_houses = len(nums)
        m = {}

        def visit(i):
            if i >= num_houses:
                return 0

            if i in m:
                return m[i]

            if i == num_houses - 1 or i == num_houses - 2:
                m[i] = nums[i]
                return m[i]
            
            m[i] = nums[i] + max(visit(i + 2), visit(i + 3))
            return m[i]

        return max(visit(0), visit(1))