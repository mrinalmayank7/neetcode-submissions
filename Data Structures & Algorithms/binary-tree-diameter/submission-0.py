# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.result=0
    def height(self, root: Optional[TreeNode]):
        if not root:
            return 0
        left= self.height(root.left)
        right=self.height(root.right)
        diameter = left + right
        self.result=max(self.result,diameter)
        return 1 + max(left, right)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.height(root)
        return self.result
        