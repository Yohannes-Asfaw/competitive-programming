class Solution:
    def simplifyPath(self, path: str) -> str:
        paths=path.split('/')
        stack=[]
        for i in paths:
            if i!=".." and i!="" and i!='.':
                stack.append(i)
            if stack and i=="..":
                stack.pop()
        return "/"+"/".join(stack)
        