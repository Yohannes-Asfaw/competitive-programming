def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res,stack=[],[]
        while (root != None or stack != None):
            while(root!=None):
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root= node.right
        return res
