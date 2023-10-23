class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack=[]
        for i in s:
            if i!='#':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
        stack1=[]
        for i in t:
            if i!='#':
                stack1.append(i)
            else:
                if stack1:
                    stack1.pop()
        return stack1==stack