class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        a = []
        res = []
        s = 0

        def visit(ii):
            nonlocal s

            if ii >= len(nums):
                return

            for i in range(ii, len(nums)):
                a.append(nums[i])
                s += nums[i]
                if s == target:
                    res.append(a.copy())
                if s < target:
                    visit(i)
                a.pop()
                s -= nums[i]

        visit(0)
        return res