# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def DFSBrute(self, root: Optional[TreeNode], val: int):
        if not root:
            return
        if root.val == val:
            self.node = root
            return
        self.DFS(root.left, val)
        self.DFS(root.right, val)

    def DFS(self, root: Optional[TreeNode], val: int):
        if not root:
            return
        if root.val == val:
            self.node = root
            return
        if val < root.val:
            self.DFS(root.left, val)
        else:
            self.DFS(root.right, val)

    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        self.node = None
        self.DFS(root, val)
        return self.node
