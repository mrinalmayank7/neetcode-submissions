# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def DFS(self,node: Optional[TreeNode])-> int:
        if not node:
            return 0
        left = self.DFS(node.left)
        right= self.DFS(node.right)
        left = left if left > 0 else 0 
        right = right if right > 0 else 0
        path = left + right + node.val
        self.best = max(self.best, path) #find current best, left and right already hold sum of connected paths using sends up
        sends_up = node.val + max (left,right) # send up node + one path
        return sends_up


    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.best = root.val
        self.DFS(root)
        return self.best


"""
Postorder = Left → Right → Root

Tree:
           1
         /   \
        2     3
       / \   / \
      4   5 6   7
     /
    8

Correct postorder order:
8, 4, 5, 2, 6, 7, 3, 1
self.best = root.val = 1
node 8:  left=0  right=0  path_here=0+8+0=8    best=max(1,8)=8    send_up=8+max(0,0)=8
node 4:  left=8  right=0  path_here=8+4+0=12   best=max(8,12)=12  send_up=4+max(8,0)=12
node 5:  left=0  right=0  path_here=0+5+0=5    best=max(12,5)=12  send_up=5+max(0,0)=5
node 2:  left=12 right=5  path_here=12+2+5=19  best=max(12,19)=19 send_up=2+max(12,5)=14
node 6:  left=0  right=0  path_here=0+6+0=6    best=max(19,6)=19  send_up=6+max(0,0)=6
node 7:  left=0  right=0  path_here=0+7+0=7    best=max(19,7)=19  send_up=7+max(0,0)=7
node 3:  left=6  right=7  path_here=6+3+7=16   best=max(19,16)=19 send_up=3+max(6,7)=10
node 1:  left=14 right=10 path_here=14+1+10=25 best=max(19,25)=25 send_up=1+max(14,10)=15

answer = self.best = 25 

self.best = running maximum
            updated whenever a better
            complete path is found
            at any node in the tree


2 rules:
1. best path turning HERE = left + me + right
2. send to parent = me + ONE best side
   (one side because path already turned here)


Time:  O(n) — every node visited once
Space: O(h) — recursion call stack
"""