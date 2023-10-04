def maxCoins(self, piles: List[int]) -> int:
        piles=sorted( piles,reverse=True)
        print(piles)
        ans=0
        j=1
        for i in range(len(piles)//3):
            ans+=piles[j]
            j+=2
        
        return ans
