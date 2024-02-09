class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        check=[0 for i in range(len(nums)+1)]
        for req in requests:
            reqstart,reqend=req
            check[reqstart]+=1
            check[reqend+1]-=1
        for i in range(1,len(check)):
            check[i]+=check[i-1]
        check.pop()
        nums.sort(reverse=True)
        check2=check.copy()
        mydict=defaultdict(list)
        for i in range(len(check)):
            mydict[check[i]].append(i)
        count=0
        check2=set(check2)
        check2=list(check2)
        check2.sort(reverse=True)
        for i in check2:
            for j in mydict[i]:
                check[j]=nums[count]
                count+=1
        for i in range(1,len(check)):
            check[i]+=check[i-1]
        ans=0
        for req in requests:
            reqstart,reqend=req
            if reqstart==0:
                ans+=check[reqend]
            else:
                ans+=check[reqend]-check[reqstart-1]
        
        return ans%(10**9+7)
        