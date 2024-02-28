# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        count=Counter()
        def dfs(node):
            if node:
                count[node.val]+=1
                dfs(node.left)
                dfs(node.right)
            return
        dfs(root)
        sortd=sorted(count.items(),key=lambda x:x[1],reverse=True)
        ans=[]
        max1=sortd[0][1]
        for i in sortd:
            if i[1]==max1:
                ans.append(i[0])
            else:
                break

        return ans
        
