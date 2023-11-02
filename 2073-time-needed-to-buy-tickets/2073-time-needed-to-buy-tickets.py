class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        tickets= deque([[i,v] for i ,v in enumerate(tickets)])
        ans=0
        while True:
            i,v=tickets.popleft()
            ans+=1
            if i==k and v-1==0:
                return ans
            if v>1:
                tickets.append([i,v-1])

        