# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = [0]
        def preorder_traversal(node):
            if node is not None:
                if node.val in range(low,high+1):
                    ans[0]+=node.val
                preorder_traversal(node.left)
                preorder_traversal(node.right)
        preorder_traversal(root)
        return ans[0]
            
        