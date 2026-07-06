# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root ==p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        if left and right:
            return root
        return left or right


"""
Why different from LCA BST:BST has ordering property — 
at every node you know exactly which direction p and q are in. 
Decision made at current node immediately. Never need to search both sides.Binary Tree has no ordering property. No way to know which side p or q is on without actually searching. Must explore both sides at every node.


Why split means current node is LCA:
If left returned something and right returned something — p was found on one side and q on the other. They diverge exactly at current node. No node deeper than current can be ancestor of BOTH since they are on opposite sides. So current node = lowest point where both exist as descendants = LCA.


Rules:
Rule A — node is None → return None
Rule B — node == p OR node == q → return node immediately (preorder check)
Rule C — recurse left fully, recurse right fully
Rule D — left and right both returned something → current node is LCA → return current (postorder decision)
Rule E — only one side returned something → LCA is inside that subtree, pass it up

DUPLICATE IN BINARY TREE: 
P & Q ARE TREE NODE & DUPLICATE POSSIBLE SO ALWAYS COMPARE BY REFERENCE NOT VAL:
EG: P == ROOT (BY REF), P.VAL == ROOT.VAL (BY VAL)


ANALYSIS OF CASE 3 (IMP):
Case 3 explained first:

When only one side returns something:
Means both p AND q were found inside that one subtree. The LCA was already determined deeper in that subtree and is bubbling up. Current node just passes it up — does nothing.
Example: p=6, q=4 in this tree:
        3
       / \
      5   1
     / \ / \
    6  2 0  8
      / \
     7   4
Both 6 and 4 are inside left subtree of 3. So right side returns None. Left side returns the LCA (which is 5). Node 3 just passes node5 up — 3 is not the LCA.

Trace p=6, q=4 — line by line:
dfs(3): recurse left and right
dfs(5): recurse left and right
dfs(6): node==p → return node6
dfs(2): recurse left and right
dfs(7): not p or q, no children → return None
dfs(4): node==q → return node4
back at dfs(2): left=None, right=node4... 

wait — dfs(7) is left of 2, dfs(4) is right of 2
back at dfs(2): left=None, right=node4 → only right returned → return node4
back at dfs(5): left=node6, right=node4 → BOTH sides returned → return node5 ✅
back at dfs(3): left=node5
dfs(1): recurse left and right
dfs(0): not p or q, no children → return None
dfs(8): not p or q, no children → return None
back at dfs(1): left=None, right=None → return None
back at dfs(3): left=node5, right=None → only left returned → return node5 ✅
answer: node5

TC/SC:
Time: O(n) — every node visited once
Space: O(h) — recursion stack
Natural fit: DFS hybrid (preorder + postorder) only. BFS cannot naturally bubble results back up through tree structure.



"""