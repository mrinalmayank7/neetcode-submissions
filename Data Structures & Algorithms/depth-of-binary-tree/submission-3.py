# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs (self, root: Optional[TreeNode], depth: int = 1)-> int:
        if root:
            if not root.left and not root.right:
                return depth
            left = self.dfs(root.left, depth +1)
            right = self.dfs(root.right, depth +1)
            return max(left,right)
        return 0
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxd = self.dfs(root)
        return maxd


    """
    def maxHeight(root):
    if not root: return 0
    left  = maxHeight(root.left)    # go down first
    right = maxHeight(root.right)   # go down first
    return 1 + max(left, right)     # compute HERE (coming up) ←
    """
        