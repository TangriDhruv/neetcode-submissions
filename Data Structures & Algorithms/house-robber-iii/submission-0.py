# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # we need to return a pair [withroot,withoutroot]

        def dfs(root):
            if not root:
                return [0,0]
            leftPair = dfs(root.left)
            rightPair = dfs(root.right)
            #Since we are reurning pairs and we choose the root we can't choose root.left or root.right we need to select
            #grandchildren hence we select without root value which is [1]
            withRoot = root.val + leftPair[1] + rightPair[1]
            withoutRoot = max(leftPair) + max(rightPair)

            return [withRoot,withoutRoot]
        
        return max(dfs(root))
            
        