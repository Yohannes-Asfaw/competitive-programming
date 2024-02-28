# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        ans=[]
        node1=root.right
        node2=root.left
        def dfs1(node):
            nonlocal ans
            if not node:
                ans.append(None)
            if node:
                ans.append(node.val)
                dfs1(node.right)
                
                dfs1(node.left)
            return ans
        ans1=[]
        def dfs2(node):
            nonlocal ans1
            if not node:
                ans1.append(None)
            
            if node:
                ans1.append(node.val)
                dfs2(node.left)
                dfs2(node.right)
            return ans1
        
        dfs1(node1)
        dfs2(node2)
        print(ans,ans1)
        return ans==ans1