class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        left=0
        count={}
        ans=float("inf")
        for right in range(len(cards)):
            if cards[right] in count:
                ans=min(ans,right-count[cards[right]]+1)
                count[cards[right]]=right
            count[cards[right]]=right
            
        if ans==float("inf"):
            return -1
        return ans            
        