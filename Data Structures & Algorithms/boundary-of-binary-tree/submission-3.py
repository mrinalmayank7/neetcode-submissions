# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result=[]
        # ADD ROOT
        result.append(root.val)

        if not root.left and not root.right:
            return result
        #DFS PREORDER: TRAVERSE LEFT BOUNDRY
        def addLeftBoundry(node):
            if not node or (not node.left and not node.right):
                return
            result.append(node.val)
            if node.left:
                addLeftBoundry(node.left)
            else:
                 #INCASE AT LEFT BOUNDRY NODE LEFT CHILD MISSING, NEXT RIGHT IS ALSO IN BOUNDRY
                addLeftBoundry(node.right)

        #DFS PREORDER: ONLY LEAVES
        def addLeaves(node):
            if not node:
                return
            if not node.left and not node.right:
                result.append(node.val)
            addLeaves(node.left)
            addLeaves(node.right)

        # DFS POSTORDER: ONLY RIGHT
        def addRightBoundry(node):
            if not node or (not node.left and not node.right):
                return
            if node.right:
                addRightBoundry(node.right)
            else:
                addRightBoundry(node.left) 
            # IN POSTDOER APPEND IS AT END 
            result.append(node.val)  

        addLeftBoundry(root.left)
        addLeaves(root) 
        addRightBoundry(root.right)
        return result

"""
Step 1: add root.val manually

Step 2: preorder on ONE path (root.left downward)
        prefer left, use right if no left
        add node BEFORE recursing
        stop at leaf

Step 3: preorder on ENTIRE tree
        add node ONLY if leaf

Step 4: postorder on ONE path (root.right downward)
        prefer right, use left if no right
        add node AFTER recursing
        stop at leaf


TC and SC:
Time: O(n) — every node visited once across all 3 functions
Space: O(h) — recursion stack

"""
                
                
                
                
                
                
                
                