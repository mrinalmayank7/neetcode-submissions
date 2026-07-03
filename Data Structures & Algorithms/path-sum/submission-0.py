# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if  not root:
            return False
        if not root.left and not root.right:
            return root.val == targetSum

        remaining =  targetSum - root.val
        left=self.hasPathSum(root.left,remaining)
        right=self.hasPathSum(root.right,remaining)
        return left or right


"""

path = root to leaf = going DOWNWARD
carrying information downward = DFS top-down (preorder)

BFS also works but not a fit or required

path sum exists when:
  at leaf: remaining sum == node.val
  OR left subtree has path with remaining sum - node.val
  OR right subtree has path with remaining sum - node.val

subtract current node value as we go down
at leaf: check if remaining == 0 (last node is equal to remaining means its subtraction will give 0)

        5
       / \
      4   8
     /
    11
   /  \
  7    2

targetSum=22

dfs(7, remaining=2):  leaf! 2==7? NO → return False
dfs(2, remaining=2):  leaf! 2==2? YES → return True
dfs(11, remaining=13): left=False, right=True → return True
dfs(8, remaining=17): leaf! 17==8? NO → return False
dfs(4, remaining=17): left=True, right=False → return True
dfs(5, remaining=22): left=True → short circuit → return True ✅

"""