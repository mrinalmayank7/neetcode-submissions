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
