class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=""
        check=strs[0]
        for i in range(len(check)):
            for j in range(1,len(strs)):
                if i==len(strs[j]) or check[i]!=strs[j][i]:
                    return ans
            ans+=check[i]
        return ans
                

                
                
            
            
        