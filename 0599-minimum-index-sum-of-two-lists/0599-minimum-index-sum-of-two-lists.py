class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dictwithindex={}
        ans={}
        minmumindexsum=float("inf")
        for i in range(len(list1)):
            dictwithindex[list1[i]]=i
        for j in range(len(list2)):
            if list2[j] in dictwithindex:
                ans[list2[j]]=dictwithindex[list2[j]]+j

        ans2=sorted(ans.items(),key=lambda x:x[1])
        ans3=[]
        minvalue=ans2[0][1]
        for i in ans2:
            if i[1]==minvalue:
                ans3.append(i[0])
        return ans3

        