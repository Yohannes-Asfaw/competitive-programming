# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans=float("-inf")
        def dfs(node):
            nonlocal ans
            if not node.right and not node.left:
                ans=max(ans,0)
                return [node.val,node.val]
            elif not node.right and node.left:
                m=dfs(node.left)
                ans=  max(ans,abs(node.val-min(node.val,m[0])),abs(node.val-max(node.val,m[1])))
                return min(node.val,m[0]),max(node.val,m[1])
            elif node.right and not node.left:
                n=dfs(node.right)
                ans=  max(ans,abs(node.val-min(node.val,n[0])),abs(node.val-max(node.val,n[1])))
                return min(node.val,n[0]),max(node.val,n[1])
            elif node.right and node.left:
                s=dfs(node.left)
                j=dfs(node.right)
                ans=max(ans,abs(node.val-min(s[0],j[0])),abs(node.val-max(s[1],j[1])))
                return min(node.val,s[0],j[0]),max(node.val,s[1],j[1])
        dfs(root)
        return ans
