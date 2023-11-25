class Solution:
    def minLength(self, s: str) -> int:
        stack=[s[0]]
        for i in range(1,len(s)):
            if stack and (stack[-1]+s[i]=="AB" or stack[-1]+s[i]=="CD"):
                stack.pop()
            else:
                stack.append(s[i])
        return len(stack)
        