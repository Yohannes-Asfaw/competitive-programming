class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        mydict=defaultdict(list)
        for i ,num in enumerate(nums):
            if len(mydict[num])==0:
                mydict[num].append(i)
            else:
                mydict[num].append(mydict[num][-1]+i)
        print(mydict)
        count=Counter()
        res=[]
        for i ,num in enumerate(nums):
            if count[num]==0:
                res.append(mydict[num][-1]-(mydict[num][count[num]])*(len(mydict[num])-count[num]))
                count[num]+=1
            else:
                res.append(((mydict[num][-1]-mydict[num][count[num]])-(mydict[num][count[num]]-mydict[num][count[num]-1])*(len(mydict[num])-count[num]-1))+((count[num]+1)*(mydict[num][count[num]]-mydict[num][count[num]-1]))-mydict[num][count[num]])
                count[num]+=1
        return res
        

        