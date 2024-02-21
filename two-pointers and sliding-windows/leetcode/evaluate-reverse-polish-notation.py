class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i not in "+-*/":
                stack.append(int(i))
            else:
                second=stack.pop()
                first=stack.pop()
                if i=="*":
                    ans=first*second
                    stack.append(ans)
                elif i=="/":
                    ans=first/second
                    if ans < 0:
                        ans=ceil(ans)
                    else:
                        ans=floor(ans)
                    stack.append(ans)
                elif i=="+":
                    ans=first+second
                    stack.append(ans)
                elif i=="-":
                    ans=first-second
                    stack.append(ans)
        return stack[-1]
