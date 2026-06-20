# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        que = deque([root])
        while que:
            for i in range(len(que)):
                curr = que.popleft()
                left = curr.left
                right = curr.right
                if left:
                    que.append(left)
                if right:
                    que.append(right)
            if curr:
                result.append(curr.val)
        return result
        