class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans=[]
        for i in range(len(prices)):
            
            for j in range(i+1,len(prices)):
                if prices[j]<=prices[i]:
                    ans.append(prices[i]-prices[j])
                    break
                elif j==len(prices)-1:
                    ans.append(prices[i])
        ans.append(prices[-1])
        return ans
        