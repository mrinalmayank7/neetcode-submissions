# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.i=1
        self.result = None
        def inorder(root,k):
            if not root or self.result:
                return
            inorder(root.left,k)
            if self.i == k:
                self.result = root.val
            self.i +=1
            inorder(root.right,k)
        inorder(root,k)
        return self.result