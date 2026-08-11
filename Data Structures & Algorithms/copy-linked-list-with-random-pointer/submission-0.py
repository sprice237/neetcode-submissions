"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cloned_nodes_by_original_nodes = {}

        def clone(node):
            if not node:
                return None

            # because the random pointer can point to any node in the list
            # (including nodes we haven't cloned yet)
            # it is impossible to set the random pointer without cloning
            # the entire list
            # so we have to do this in two passes
            # initially, we set the cloned node's random pointer
            # to the node in the original list
            # once the entire list has been cloned, we will iterate
            # through the cloned list to update the random pointer

            cloned_node = Node(node.val, clone(node.next), node.random)
            cloned_nodes_by_original_nodes[node] = cloned_node

            return cloned_node

        cloned_head = clone(head)

        def update_random(node):
            if not node:
                return None

            node.random = cloned_nodes_by_original_nodes.get(node.random)

            update_random(node.next)

        update_random(cloned_head)

        return cloned_head
