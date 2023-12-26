class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans1=[]
        ans2=[]
        arr2set=set(arr2)
        dicta={}
        for i in arr1:
            if i not in dicta:
                dicta[i]=1
            else:
                dicta[i]+=1
        for i in arr2:
            ans1+=[i]*dicta[i]
        for i in arr1:
            if i not in arr2set:
                ans2.append(i)
        return ans1+sorted(ans2)