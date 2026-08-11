# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def traverse(node):
            if node.val == p or node.val == q:
                return node
            
            if p.val < node.val and q.val < node.val:
                traverse_result = traverse(node.left)
            elif p.val > node.val and q.val > node.val:
                traverse_result = traverse(node.right)
            else:
                traverse_result = None

            return traverse_result or node

        return traverse(root)