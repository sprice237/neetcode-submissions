# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def traverse(node):
            if p.val < node.val and q.val < node.val:
                return traverse(node.left)
            if p.val > node.val and q.val > node.val:
                return traverse(node.right)
            return node


        return traverse(root)