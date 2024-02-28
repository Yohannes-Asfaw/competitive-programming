# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node1,node2):
            if not node1 and not node2:
                return None
            if node1:
                v1=node1.val
            else:
                v1=0
            if node2:
                v2=node2.val
            else:
                v2=0
            new=TreeNode(v1+v2)
            new.left=dfs(node1.left if node1 else None,node2.left if node2 else None)
            new.right=dfs(node1.right if node1 else None,node2.right if node2 else None)
            return new
        return dfs(root1,root2)


            