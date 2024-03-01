# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        res=0
        def dfs(node):
            nonlocal res
            if not node:
                return float("inf"),float("-inf"),0
            if node:
                left=dfs(node.left)
                right=dfs(node.right)
                if left[1]>=node.val or right[0]<=node.val:
                    return float("-inf"),float("inf"),0
                sum=left[2]+node.val+right[2]
                res=max(res,sum)
                return min(left[0],node.val),max(right[1],node.val),sum
            
        dfs(root)
        return res
                