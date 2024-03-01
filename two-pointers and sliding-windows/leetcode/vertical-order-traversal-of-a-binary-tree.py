# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]
        def dfs(node,c,r):
            nonlocal ans
            if node:
                ans.append([c,r,node.val])
                dfs(node.left,c-1,r+1)
                dfs(node.right,c+1,r+1)
            return 
        dfs(root,0,0)
        res=[]
        ans=sorted(ans,key=lambda x:(x[0],x[1],x[2]))
        dictionary=defaultdict(list)
        for i,j,k in ans:
            dictionary[i].append(k)
        for i in dictionary.values():
            res.append(i)
        return res

        