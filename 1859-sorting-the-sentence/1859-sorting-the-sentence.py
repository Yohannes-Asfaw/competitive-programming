class Solution:
    def sortSentence(self, s: str) -> str:
        dictionary={}
        list1=s.split()
        list1.sort(key= lambda x:x[-1])
        ans=[]
        for i in list1:
            ans.append(i[:-1])
        return " ".join(ans)
        

        