class Solution:
    def decodeString(self, s: str) -> str:
        def find(s,i):
            res=""
            n=0
            mul=''
            while i<len(s):
                if  s[i].isdigit():
                    n = n*10+int(s[i])
                    i+=1
                elif s[i]=="[":
                    new,i=find(s,i+1)
                    res+=n*new
                    n=0
                    i+=1
                elif s[i]=="]":
                    return (res,i)
                    i+=1
                else:
                    res+=s[i]
                    i+=1
            return (res,i)
        return find(s,0)[0]
        