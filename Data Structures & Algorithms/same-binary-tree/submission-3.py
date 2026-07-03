# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
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
    def isSameTreedffs(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            left = self.isSameTree(p.left,q.left)
            right = self.isSameTree(p.right,q.right)
            return left and right
        return False