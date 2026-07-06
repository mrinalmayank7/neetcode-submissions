# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        if (p.val < root.val and q.val < root.val):
            return self.lowestCommonAncestor(root.left, p,q)
        if (p.val > root.val and q.val > root.val):
            return self.lowestCommonAncestor(root.right, p,q)
        return root
                
"""
Three cases — complete rules:
Case 1: both p and q < current → go left, LCA is somewhere in left subtree
Case 2: both p and q > current → go right, LCA is somewhere in right subtree
Case 3: p < current < q OR current == p OR current == q → current IS the LCA

Brute  = plain binary tree LCA approach → O(n) time O(n) space
Optimal = BST property navigation (LC 235) → O(h) time O(h) space
more space optimiozation: o(1) use iterative 
"""
                