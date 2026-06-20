# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        que = deque([root])

        while que:
            curr = que.popleft()
            curr.left,curr.right = curr.right,curr.left
            if curr.left:
                que.append(curr.left)
            if curr.right:
                que.append(curr.right)
        return root
