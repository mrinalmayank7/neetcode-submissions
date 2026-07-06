# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val > key:
            root.left = self.deleteNode(root.left,key)
        elif root.val < key:
            root.right = self.deleteNode(root.right,key)  
        else:
            #CASE 1
            if not root.left and not root.right:
                return None
            #case 2
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            successor = root.right
            while successor.left:
                successor=successor.left
            root.val = successor.val
            root.right = self.deleteNode(root.right,successor.val)

        return root      


"""
TC/SC:
Brute: O(n) — plain DFS ignore BST property
Optimal: O(h) time, O(h) space recursive / O(1) space iterative


Case 1 — node to delete is a LEAF (no children):
  simply remove it → return None to parent

Case 2 — node to delete has ONE child:
  replace node with its only child
  return that child to parent

Case 3 — node to delete has TWO children:
  cannot simply remove → tree would split into two
  need a replacement node that maintains BST property
  replacement = inorder successor (smallest node in right subtree)
  copy successor's value into current node
  delete successor from right subtree (successor is always a leaf or has one right child)
"""