# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        que = deque([root])

        while que:
            ans =[]
            for _ in range(len(que)):
                curr = que.popleft()
                ans.append(curr.val)
                if curr.left:
                    que.append(curr.left)
                if curr.right:
                    que.append(curr.right)
            result.append(ans)
        
        return result

            

        