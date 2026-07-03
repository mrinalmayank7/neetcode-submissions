# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result=[]
        reverse=False
        queue=deque([root])
        while queue:
            size=len(queue)
            level=[]
            for _ in range(size):
                node=queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if reverse:
                level.reverse() 
            result.append(level)  
            reverse = False if reverse else True

        return result

    def DFS(self, root: Optional[TreeNode], depth, result):
        if not root:
            return
        if depth == len(result): # depth changed
            result.append([])#add new empty level
        result[depth].append(root.val) #at depth (which is used as level, append numbers)
        self.DFS(root.left,depth+1,result)
        self.DFS(root.right,depth+1,result)

    def zigzagLevelOrderDFS(self, root: Optional[TreeNode]) -> List[List[int]]:
        result=[]
        self.DFS(root,0,result)
        for i in range(1,len(result),2):
            result[i].reverse()
        return result
"""
BFS: same as level order BUT reverse after each step
DFS: Works same as finding lvel using depth with result lenght
- if found append an empty list in result
- depth = level, means result[depth] will append values at the level index
- at end → reverse odd levels in main function

Time:  O(n) — visit every node once
Space: O(n) — result stores all nodes
       O(w) BFS queue — balanced O(n)
       O(h) DFS stack — balanced O(logn)
"""
