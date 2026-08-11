# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def count_good_nodes(n, m):
            if not n:
                return 0
            v = 1 if m is None or n.val >= m else 0
            m = max(m, n.val) if m is not None else n.val
            return v + count_good_nodes(n.left, m) + count_good_nodes(n.right, m)

        return count_good_nodes(root, None)