class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        dic={}
        dic["("]=")"
        count=0
        for i in s:
            if i in dic.keys():
                stack.append(i)
            else:
                if stack and dic[stack[-1]]==i:
                    stack.pop()
                    continue
                else:
                    count+=1
                

        return count+len(stack)

        
        