class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while r - l > 1 and nums[r] < nums[l]:
            m = (l + r) // 2
            
            if nums[m] > nums[l]:
                l = m
            elif nums[m] < nums[r]:
                r = m


        return min(nums[l], nums[r])
