# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Calculate the height of left subtree and right subtree
    # and then the difference, if difference >1 return -1
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return 0
            
            left = dfs(root.left)
            
            # even when I say left it goes through complete left subtree and calculate left and right values of left subtree
            if left == -1:
                return -1
            # same with right
            right = dfs(root.right)
            if right == -1:
                return -1
            if (abs(left-right)>1):
                return -1
            # below return statement is how you calculate height of a tree.
            return 1+max(left,right)
        return dfs(root) != -1
        