# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: 
            return None
        # root.left, root.right = root.right, root.left #preorder also works
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left, root.right = root.right, root.left # postorder also works

        return root
    def invertTreeBFS(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        queue= deque([root])
        while queue:
            node = queue.popleft()
            node.left, node.right = node.right,node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
        return root
"""
DFS
Does order matter here?

PREORDER (swap before going down):
  swap at node 1 first
  then recurse into children

POSTORDER (swap after children done):
  recurse into children first
  then swap at current node

BOTH work for invert!
swapping at any point gives same result
preorder is slightly more intuitive


BFS invert = level by level swap
DFS invert = node by node swap going deep

Both correct
BFS makes the "level by level mirroring"
visually obvious

Time:  O(n) — visit every node once
Space: O(h/w) — recursion call stack
              balanced → O(logn)
              skewed   → O(n)

"""
        