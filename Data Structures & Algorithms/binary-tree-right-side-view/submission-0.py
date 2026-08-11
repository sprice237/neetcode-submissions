# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # to be visible on the right side, the node needs to be the last node in its level
        # walk the tree using BFS, and append the node to the return list if it's the last in its level
        # we know if its the last in its level by
        #   1) tracking the level of each node alongside the node in the queue
        #   2) peeking at the level of the next node in the queue
        #   3) if the next node is at a higher level (or there is no next node), then
        #      our current node is the last in its level, and therefore visible from the right

        if not root:
            return []

        q = [[root, 0]]
        right_side_nodes = []

        def walk():
            if not q:
                return

            [n, level] = q.pop(0)

            if n.left:
                q.append([n.left, level + 1])
            if n.right:
                q.append([n.right, level + 1])

            try:
                next_node, next_level = q[0]
                if next_level > level:
                    right_side_nodes.append(n.val)
            except IndexError:
                right_side_nodes.append(n.val)

            walk()

        walk()

        return right_side_nodes

        