# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []

        n = root
        while n:
            self.stack.append((n, False))
            n = n.left
        
    def print_stack(self):
        print([(n[0].val, n[1]) for n in self.stack])

    def next(self) -> int:
        (ret_n, _) = self.stack.pop()

        if ret_n.right:
            self.stack.append((ret_n, True))
            n = ret_n.right
            while n:
                self.stack.append((n, False))
                n = n.left
        else:
            while self.stack and self.stack[-1][1]:
                self.stack.pop()

        return ret_n.val

    def hasNext(self) -> bool:
        return not not self.stack
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()