# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.i=0
        self.result = None
        def inorder(root,k):
            if not root or self.result:
                return
            
            inorder(root.left,k)
            self.i +=1
            if self.i == k:
                self.result = root.val
                return
            inorder(root.right,k)
        inorder(root,k)
        return self.result

"""
DFS INORDER: AS INORDER IS IN SORTED ORDER
I IS POSITION IF CURRENT VAL, IF WE REACH K, I = K, NODE AT K IS ANS

Time: O(h + k) — h to reach leftmost node, k steps of inorder after that. Not O(n) because stops exactly at kth element.
Space: O(h) — recursion stack.


The brute-force approach is:
Perform a complete inorder traversal.
Store all node values in an array.
Return array[k - 1].
Complexity
Time: O(n) (visit every node)
Space: O(n) (store all values)
"""