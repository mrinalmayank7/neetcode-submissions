# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.answer=True
        self.height(root)
        return self.answer
    def height(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        left  = self.height(node.left)
        right = self.height(node.right)

        if abs(left - right) > 1:
            self.answer = False
        return 1 + max(left, right)


"""
        1
       / \
      2   3
     / \
    4   5

height(4): leaf → return 1
height(5): leaf → return 1
height(2): left=1, right=1
           |1-1|=0 ≤ 1 
           return 1+max(1,1) = 2

height(3): leaf → return 1
height(1): left=2, right=1
           |2-1|=1 ≤ 1 
           return 1+max(2,1) = 3

result != -1 → True 
"""