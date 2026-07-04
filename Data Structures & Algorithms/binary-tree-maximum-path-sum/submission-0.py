# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.best = root.val

        def dfs(node):
            if not node:
                return 0

            left  = dfs(node.left)
            right = dfs(node.right)

            # ignore negative contributions
            left  = left  if left  > 0 else 0
            right = right if right > 0 else 0

            # Thing 1: best path THROUGH this node
            self.best = max(self.best, left + node.val + right)

            # Thing 2: offer to parent — ONE side only
            return node.val + max(left, right)

        dfs(root)
        return self.best