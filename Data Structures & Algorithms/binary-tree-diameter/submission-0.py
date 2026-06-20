# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        def dfs (root):
            if not root:
                return 0
            left_subtree = dfs(root.left)
            right_subtree = dfs(root.right)
            self.diameter = max(self.diameter,left_subtree+right_subtree)
            return 1+ max(left_subtree,right_subtree)
        dfs(root)
        return self.diameter


        
        