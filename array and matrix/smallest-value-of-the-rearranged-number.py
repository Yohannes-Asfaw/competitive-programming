class Solution:
    def smallestNumber(self, num: int) -> int:
        if num>0:
            num=str(num)
            zeros=num.count("0")
            ans=[]
            for i in num:
                if i !="0":
                    ans.append(i)
            ans.sort()
            newans=ans[0]+"0"*zeros+"".join(ans[1:])
            return int(newans)
        else:
            num=str(num)
            ans=[]
            for i in num:
                if i !="-":
                    ans.append(i)
            ans.sort(reverse=True)
            if int("".join(ans))!=0:
                return int("".join(ans))*-1
            return int("".join(ans))
            
        