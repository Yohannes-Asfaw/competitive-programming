# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxdepth=0
        if not root:
                return maxdepth
        def dfs(node,count):
            nonlocal maxdepth
            maxdepth=max(count,maxdepth)
            if node:
                dfs(node.left,count+1)
                dfs(node.right,count+1)
            count-=1
            return maxdepth
        dfs(root,0)
        return maxdepth
        
