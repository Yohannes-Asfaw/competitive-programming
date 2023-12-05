class Solution:
    def largestGoodInteger(self, num: str) -> str:
        maxint=float("-inf")
        i=0
        j=3
        while j<=len(num):
            if len(set(num[i:j]))==1:
                maxint=max(maxint,int(num[i:j]))
            i+=1
            j+=1
        if str(maxint)=="0":
            return str(maxint)*3
        elif maxint==float("-inf"):
            return ""
        else:
            return str(maxint)
        