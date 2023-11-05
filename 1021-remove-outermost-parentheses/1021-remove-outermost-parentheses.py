class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack=[]
        new=""
        ans=""
        for icon in s:
            new+=icon
            if icon=="(":
                stack.append(icon)
            elif icon==")":
                stack.pop()
            if len(stack)==0:
                ans+=new[1:len(new)-1]
                new=""
        return ans
