class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # current_sum tracks the maximum possible subarray sum of all
        # numbers leading up to (and including) the number under consideration
        # we initialize it to zero to not bias the sum when we add numbers to it
        current_sum = 0

        # max_sum tracks the largest subarray sum of any subarray that has
        # been encountered
        max_sum = nums[0]

        for n in nums:
            # if current_sum is negative, set it to 0
            # (we will exclude all numbers that have come before)
            current_sum = max(current_sum, 0)

            # add the current number to current_sum
            current_sum += n

            # if current_sum is larger than the current max_sum, use it
            max_sum = max(current_sum, max_sum)

        return max_sum