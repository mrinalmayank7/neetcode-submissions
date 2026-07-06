# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        path=[]
        result=[]
        def dfs(node, remaining):
            if not node :
                return
            path.append(node.val)
            remaining = remaining - node.val

            if not node.left and not node.right:
                if remaining == 0:
                    result.append(path[:])#if we use path , it will point to same memory, [:] create a shallow copy
            else:
                dfs(node.left,remaining)
                dfs(node.right,remaining)
            path.pop()

        dfs(root,targetSum)
        return result

"""
DFS With backtracking
Time: O(n^2) — every node visited once
Space: O(h^2) — recursion stack depth = height of tree. Plus O(n) for storing all valid paths in result.
Rules:

A — CHOOSE: append node.val to path, subtract from remaining
B — EXPLORE: recurse left then right
C — UNDO: path.pop() after BOTH children return (always runs, valid or invalid — because next branch must see clean path without current node)
D — Valid leaf: remaining==0 → append copy to result
E — Invalid leaf: remaining≠0 → just return, undo happens
        5
       / \
      4   8
     /   / \
    11  13   4
   /  \     / \
  7    2   5   1
target = 22

dfs(5, rem=22):
  CHOOSE: path=[5], rem=22-5=17
  EXPLORE left → dfs(4, rem=17)

dfs(4, rem=17):
  CHOOSE: path=[5,4], rem=17-4=13
  EXPLORE left → dfs(11, rem=13)

dfs(11, rem=13):
  CHOOSE: path=[5,4,11], rem=13-11=2
  EXPLORE left → dfs(7, rem=2)

dfs(7, rem=2):
  CHOOSE: path=[5,4,11,7], rem=2-7=-5
  leaf, rem=-5≠0 → INVALID
  UNDO: path=[5,4,11]
  return

  EXPLORE right → dfs(2, rem=2)

dfs(2, rem=2):
  CHOOSE: path=[5,4,11,2], rem=2-2=0
  leaf, rem=0 → VALID ✅ → result=[[5,4,11,2]]
  UNDO: path=[5,4,11]
  return

  both children done
  UNDO: path=[5,4]
  return

  EXPLORE right → dfs(None, rem=13) → return immediately
  both children done
  UNDO: path=[5]
  return

  EXPLORE right → dfs(8, rem=17)

dfs(8, rem=17):
  CHOOSE: path=[5,8], rem=17-8=9
  EXPLORE left → dfs(13, rem=9)

dfs(13, rem=9):
  CHOOSE: path=[5,8,13], rem=9-13=-4
  leaf, rem=-4≠0 → INVALID
  UNDO: path=[5,8]
  return

  EXPLORE right → dfs(4, rem=9)

dfs(4, rem=9):
  CHOOSE: path=[5,8,4], rem=9-4=5
  EXPLORE left → dfs(5, rem=5)

dfs(5, rem=5):
  CHOOSE: path=[5,8,4,5], rem=5-5=0
  leaf, rem=0 → VALID ✅ → result=[[5,4,11,2],[5,8,4,5]]
  UNDO: path=[5,8,4]
  return

  EXPLORE right → dfs(1, rem=5)

dfs(1, rem=5):
  CHOOSE: path=[5,8,4,1], rem=5-1=4
  leaf, rem=4≠0 → INVALID
  UNDO: path=[5,8,4]
  return

  both children done
  UNDO: path=[5,8]
  return

  both children done
  UNDO: path=[5]
  return

  both children done
  UNDO: path=[]
  return

result = [[5,4,11,2], [5,8,4,5]] ✅
"""
