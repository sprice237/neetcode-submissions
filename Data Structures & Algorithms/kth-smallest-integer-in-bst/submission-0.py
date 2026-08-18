# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class ResultException(Exception):
    def __init__(self, value):
        self.value = value

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        num_nodes_visited = 0

        def dfs(node):
            nonlocal num_nodes_visited
            
            if node.left:
                dfs(node.left)

            num_nodes_visited += 1

            if num_nodes_visited == k:
                raise ResultException(node.val)

            if node.right:
                dfs(node.right)

        try:
            dfs(root)
        except ResultException as e:
            return e.value