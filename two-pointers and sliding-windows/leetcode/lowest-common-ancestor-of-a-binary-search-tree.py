# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node,val1,val2):
            if node:
                if val1>node.val and val2>node.val:
                    return dfs(node.right,val1,val2)
                elif val1<node.val and val2<node.val:
                    return dfs(node.left,val1,val2)
                elif (val1>node.val and val2<node.val) or (val1<node.val and val2>node.val):
                    return node
                elif val1==node.val:
                    return node
                elif val2==node.val:
                    return node
        return dfs(root,p.val,q.val)
