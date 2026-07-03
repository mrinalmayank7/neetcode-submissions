# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def DFS(self, root: Optional[TreeNode], depth, result):
        if not root:
            return
        if depth == len(result):
            result.append(root.val)
        self.DFS(root.right,depth+1,result)
        self.DFS(root.left,depth+1,result)
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        self.DFS(root, 0, result)
        return result
    def rightSideViewBFS(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        if not root:
            return []
        queue=deque([root])
        while queue:
            size=len(queue)
            for _ in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                right_node =  node.val
            result.append(right_node) 
        return result

"""
BFS: Direct implementation of BFS, just result stores last node of level

DFS: PREORDER (Idea: when first time depth changes append list element from right side )
  so at any node:
  if len(result) == depth → this level not stored yet → first visit
  if len(result) > depth → this level already stored → skip
ALSO VISIT RIGHT FIRST

depth=0 (root level):
  before visiting root → result=[] → len=0
  0 == 0 → first visit → append ✅

depth=1 (second level):
  node 3 visited first (right child of root)
  result=[1] → len=1
  1 == 1 → first visit at depth=1 → append 3 ✅

  node 2 visited second (left child of root)
  result=[1,3] → len=2
  2 != 1 → depth=1 already stored → skip ✅

depth=2:
  node 5 visited
  result=[1,3] → len=2
  2 == 2 → first visit at depth=2 → append 5 ✅


Time:  O(n) — visit every node once
Space: O(h) DFS  — recursion stack
       O(w) BFS  — queue width
       balanced: DFS O(logn), BFS O(n)
       skewed:   DFS O(n),    BFS O(1)
"""
