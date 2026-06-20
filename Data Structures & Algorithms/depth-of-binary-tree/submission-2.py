# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        q = deque([root])
        count = 0

        while q:
            for i in range(len(q)):
                curr = q.popleft()
                left = curr.left
                right = curr.right
                if left:
                    q.append(left)
                if right:
                    q.append(right)
            count = count+1
        return count
