# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root: Optional[TreeNode],result)-> None:
        if root:
            self.dfs(root.left,result)
            result.append(root.val)
            self.dfs(root.right,result)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        self.dfs(root,result)
        return result

"""
TRACE INRODER:
dfs(1)
  dfs(2)
    dfs(4)
      dfs(None) → return
      append 4       result=[4]
      dfs(None) → return
    append 2         result=[4,2]
    dfs(5)
      dfs(None) → return
      append 5       result=[4,2,5]
      dfs(None) → return
  append 1           result=[4,2,5,1]
  dfs(3)
    dfs(None) → return
    append 3         result=[4,2,5,1,3]
    dfs(None) → return

return [4,2,5,1,3]
"""
"""
PREORDER
    result.append(root.val)
    self.dfs(root.left,result)
    self.dfs(root.right,result)

POSTORDER
    self.dfs(root.left,result)
    self.dfs(root.right,result)
    result.append(root.val)

Time:  O(n) — every node visited once
Space: O(h) — recursion call stack
              balanced → O(logn)
              skewed   → O(n)
"""