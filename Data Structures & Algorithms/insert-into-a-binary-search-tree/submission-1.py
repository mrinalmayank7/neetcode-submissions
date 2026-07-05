# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
            
        if   val < root.val:
            root.left = self.insertIntoBST(root.left,val)
        else:
            root.right= self.insertIntoBST(root.right,val)
        return root
"""
 O(h) time O(h) space

        4
       / \
      2   7
         /
        6
insert 5

insertIntoBST(4, 5): 5>4 → root.right = insertIntoBST(7, 5)
insertIntoBST(7, 5): 5<7 → root.left = insertIntoBST(6, 5)
insertIntoBST(6, 5): 5<6 → root.left = insertIntoBST(None, 5)
insertIntoBST(None, 5): root is None → return TreeNode(5)
back at insertIntoBST(6): root.left = TreeNode(5), return node6
back at insertIntoBST(7): root.left = node6, return node7
back at insertIntoBST(4): root.right = node7, return node4
result: 5 inserted as left child of 6 
"""