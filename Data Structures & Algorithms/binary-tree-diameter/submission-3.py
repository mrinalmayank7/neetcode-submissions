# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def height(self, root: Optional[TreeNode]):
        if not root:
            return 0
        left= self.height(root.left)
        right=self.height(root.right)
        diameter = left + right
        self.result=max(self.result,diameter)
        return 1 + max(left, right)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result=0
        self.height(root)
        return self.result

"""
diameter at any node = left_height + right_height
                       (number of edges through this node)

answer = MAX of this across ALL nodes

height returns upward (parent needs it)
diameter stored in self.result (no one returns it, just tracked)


1
       / \
      2   3
     / \
    4   5

self.result = 0 initially

height(4): leaf → return 1,  diameter=0+0=0, result=max(0,0)=0
height(5): leaf → return 1,  diameter=0+0=0, result=max(0,0)=0
height(2): left=1, right=1
           diameter = 1+1 = 2
           result = max(0,2) = 2 
           return 1+max(1,1) = 2

height(3): leaf → return 1,  diameter=0+0=0, result=max(2,0)=2
height(1): left=2, right=1
           diameter = 2+1 = 3
           result = max(2,3) = 3 
           return 1+max(2,1) = 3

answer = self.result = 3 

Time:  O(n) — visit every node once
Space: O(h) — recursion call stack
              balanced → O(logn)
              skewed   → O(n)

Only 1 solution — no brute/optimal:
  must visit every node
  O(n) is the only option
"""
        