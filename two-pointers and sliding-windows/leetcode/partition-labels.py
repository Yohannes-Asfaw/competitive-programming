class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        index_dic={}
        for i in range(len(s)):
            index_dic[s[i]]=i
        maxindex=float("-inf")
        ans=[]
        for i in range(len(s)):
            maxindex=max(maxindex,index_dic[s[i]])
            if maxindex==i:
                if ans:
                    ans.append(i-last)
                    last=i
                else:
                    
                    ans.append(i+1)
                    last=i
                
                maxindex=0


                
        return ans
        