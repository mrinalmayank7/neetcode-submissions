"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        queue= deque([root])
        while queue:
            nextnode=None
            size=len(queue)
            for _ in range(size):
                node=queue.popleft()
                node.next=nextnode
                nextnode=node
                #RIGHT TO LEFT 
                # 3 POINT TO NONE
                # 2 POINT TO 3
                # WONT WORK FROM LEFT TO RIGHT
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)     

        return root

"""
Natural fit: BFS — level by level connection. DFS needs level tracking — unnatural.

RIGHT:
Core idea — why right to left:
next pointer means each node points to RIGHT neighbor. To set right neighbor correctly using a nextnode variable — you need to process nodes RIGHT TO LEFT. Because:
processing right to left:
  when you process node X → nextnode is already set to node on X's RIGHT
  so X.next = nextnode = correct right neighbor 

WRONG:
processing left to right:
  when you process node X → nextnode is the node on X's LEFT
  so X.next = nextnode = wrong neighbor 
To process right to left — add RIGHT child before LEFT child to queue. Queue then naturally holds nodes right to left at every level.

Brute vs Optimal:
BFS with queue → O(n) time O(w) space where w = max width
O(1) space → use already set next pointers to traverse without queue → O(n) time O(1) space
"""
    