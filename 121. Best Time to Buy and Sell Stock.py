def maxProfit(self, prices: List[int]) -> int:
        max1=prices[0]
        min1=prices[0]
        maxprofit=0
        for i in range(1,len(prices)):
            if prices[i]<min1:
                min1=prices[i]
                max1=min1
            if prices[i]>max1:
                max1=prices[i]
            maxprofit=max(maxprofit,max1-min1)
        return(maxprofit)
