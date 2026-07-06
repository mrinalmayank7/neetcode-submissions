# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #APPROACH 1 - DFS PREORDER
        def valid(node,left,right):
            if not node:
                return True
            if not (left < node.val < right):
                return False
            return valid(node.left,left ,node.val) and valid(node.right, node.val,right)
        #return valid(root,float("-inf"), float("+inf"))

        #APPROACH 2 -DFS INORDER
        self.prev=None
        def inorder(node):
            if  not node:
                return True
            if not inorder(node.left):
                return False
            if self.prev is not None and node.val <= self.prev:
                return False
            self.prev = node.val
            return inorder(node.right)
        return inorder(root)
        
"""


Why two approaches exist:

BST has one golden property: inorder traversal = strictly ascending sorted sequence.

This one property can be exploited in two completely different ways:

Approach 1 — Preorder + min/max:
  check each node against valid range inherited from ancestors
  decide at current node FIRST → preorder
  
Approach 2 — Inorder + prev:
  traverse in sorted order, check each value > previous value
  process left fully FIRST → then check current → inorder
Both O(n) time O(h) space. Both correct. Different mental models.

APPROACH 1 — Preorder + min/max range

Rules:
Rule A — node is None → return True
Rule B — not (min < node.val < max) → return False
Rule C — go left: node.val becomes new upper bound, min unchanged
Rule D — go right: node.val becomes new lower bound, max unchanged
Rule E — return left AND right both True

Trace — invalid BST:

        5
       / \
      1   6
         /
        3
valid(5, -inf, +inf): -inf<5<+inf ✅ go left and right
valid(1, -inf, 5): -inf<1<5 ✅ go left and right
valid(None, -inf, 1): return True
valid(None, 1, 5): return True
back at valid(1): True and True → return True
valid(6, 5, +inf): 5<6<+inf ✅ go left and right
valid(3, 5, 6): 5<3? NO → return False ✅
back at valid(6): False → return False
back at valid(5): True and False → return False ✅
answer: False
Trace — valid BST:

        4
       / \
      2   7
     / \
    1   3
valid(4, -inf, +inf): -inf<4<+inf ✅ go left and right
valid(2, -inf, 4): -inf<2<4 ✅ go left and right
valid(1, -inf, 2): -inf<1<2 ✅ go left and right
valid(None,...): True, valid(None,...): True → return True
valid(3, 2, 4): 2<3<4 ✅
valid(None,...): True, valid(None,...): True → return True
back at valid(2): True and True → return True
valid(7, 4, +inf): 4<7<+inf ✅
valid(None,...): True, valid(None,...): True → return True
back at valid(4): True and True → return True ✅
answer: True
Code — Approach 1:


APPROACH 2 — Inorder + prev variable

Core idea:

Inorder traversal of valid BST produces strictly ascending sequence. So traverse inorder and at each node check: is current value strictly greater than previous value? If any node violates this → not valid BST.
No range needed. No -inf/+inf. Just track one previous value.

Rules:
Rule A — node is None → return True
Rule B — recurse left first, if False → return False immediately
Rule C — check current node: if prev is not None and node.val <= prev → return False
Rule D — update prev = node.val
Rule E — recurse right, return result

Trace — invalid BST:

        5
       / \
      1   6
         /
        3
inorder(5): go left first → inorder(1)
inorder(1): go left first → inorder(None) → True
inorder(1): prev=None, no check → prev=1, go right → inorder(None) → True
back at inorder(1): return True
inorder(5): prev=1, 5>1 ✅ prev=5, go right → inorder(6)
inorder(6): go left first → inorder(3)
inorder(3): go left first → inorder(None) → True
inorder(3): prev=5, 3<=5 → return False ✅
back at inorder(6): False → return False
back at inorder(5): False → return False ✅
answer: False
Trace — valid BST:

        4
       / \
      2   7
     / \
    1   3
inorder(4): go left → inorder(2)
inorder(2): go left → inorder(1)
inorder(1): go left → inorder(None) → True
inorder(1): prev=None, no check → prev=1, go right → inorder(None) → True
back at inorder(1): return True
inorder(2): prev=1, 2>1 ✅ prev=2, go right → inorder(3)
inorder(3): go left → inorder(None) → True
inorder(3): prev=2, 3>2 ✅ prev=3, go right → inorder(None) → True
back at inorder(3): return True
back at inorder(2): return True
inorder(4): prev=3, 4>3 ✅ prev=4, go right → inorder(7)
inorder(7): go left → inorder(None) → True
inorder(7): prev=4, 7>4 ✅ prev=7, go right → inorder(None) → True
back at inorder(7): return True
back at inorder(4): return True ✅
answer: True


TC/SC both approaches:
Time: O(n) — every node visited once
Space: O(h) — recursion stack
Brute: O(n²) — check entire subtree at every node
Natural fit: DFS only
"""

        

