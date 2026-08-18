# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_valid(node, left_bound, right_bound):
            if not node:
                return True

            if left_bound is not None and node.val <= left_bound:
                return False
            
            if right_bound is not None and node.val >= right_bound:
                return False

            return is_valid(node.left, left_bound, node.val) and is_valid(node.right, node.val, right_bound)

        return is_valid(root, None, None)