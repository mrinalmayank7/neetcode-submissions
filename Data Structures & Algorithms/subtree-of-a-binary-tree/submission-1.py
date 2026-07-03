# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.val == subRoot.val:   # value matches → check full subtree
                if self.isSameTreeBFS(node, subRoot):
                    return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False

    def isSameTreeBFS(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_queue= deque([p])
        q_queue =deque([q])
        while p_queue and q_queue:
            pnode = p_queue.popleft()
            qnode = q_queue.popleft()
            if not pnode and not qnode:      
                continue
            if not pnode or not qnode:      
                return False
            if pnode.val != qnode.val:
                return False
            p_queue.append(pnode.left)
            q_queue.append(qnode.left)
            p_queue.append(pnode.right)
            q_queue.append(qnode.right)
        return True


