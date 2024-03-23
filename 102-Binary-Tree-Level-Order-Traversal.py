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
        q = deque([root])
        finalAns = []
        while q:
            qlen = len(q)
            ans = []
            for i in range(qlen):
                node = q.popleft()
                if node:
                    ans.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if ans:        
                finalAns.append(ans)
        return finalAns            
        