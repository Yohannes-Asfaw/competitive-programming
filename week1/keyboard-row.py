class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        dic={}
        firstrow="qwertyuiopQWERTYUIOP"
        secondrow="asdfghjklASDFGHJKL"
        thirdrow="zxcvbnmZXCVBNM"
        for i in firstrow:
            dic[i]=1
        for i in secondrow:
            dic[i]=2
        for i in thirdrow:
            dic[i]=3
        ans=[]
        check=[]
        for i in words:
            check=[]
            for j in i:
                check.append(dic[j])
            if len(set(check))==1:
                ans.append(i)
        return ans
