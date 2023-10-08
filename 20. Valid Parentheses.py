def isValid(self, s: str) -> bool:
        stack=[]
        dic={}
        dic["{"]="}"
        dic["("]=")"
        dic["["]="]"
        for i in s:
            if i in dic.keys():
                stack.append(i)
            else:
                if stack and dic[stack[-1]]==i:
                    stack.pop()
                    continue
                else:
                    return False
        if len (stack)==0:
            return True
        else:
            return False
