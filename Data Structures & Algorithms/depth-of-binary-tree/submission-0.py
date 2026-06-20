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
        count = 0
        queue = deque([root])
        while queue:
            for i in range(len(queue)):
                curr = queue.popleft()
            
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            count = count+1
        return count

        