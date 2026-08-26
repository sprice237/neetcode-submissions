# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        overall_max = None
        def max_path_sum_for_node(node):
            nonlocal overall_max

            if not node:
                return 0

            left_path_sum = max_path_sum_for_node(node.left)
            right_path_sum = max_path_sum_for_node(node.right)

            max_segment_sum = max(left_path_sum + node.val, right_path_sum + node.val, node.val)
            max_path_sum = max(max_segment_sum, left_path_sum + right_path_sum + node.val)
            overall_max = max(max_path_sum, overall_max) if overall_max is not None else max_path_sum

            return max_segment_sum

        max_path_sum_for_node(root)

        return overall_max