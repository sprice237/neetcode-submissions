class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []

        remaining_num_indexes = set([i for i in range(len(nums))])
        current_permutation = []

        def loop(stack):
            if not remaining_num_indexes:
                permutations.append(list(current_permutation))
                return

            for i in list(remaining_num_indexes):
                current_permutation.append(nums[i])
                remaining_num_indexes.remove(i)
                loop(stack + [i])
                remaining_num_indexes.add(i)
                current_permutation.pop()

        loop([])

        return permutations