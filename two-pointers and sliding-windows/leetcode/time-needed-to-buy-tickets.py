class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue=deque([i,num] for i ,num in enumerate(tickets))
        ans=0
        while True:
            if queue[0][1]-1==0 and queue[0][0]==k:
                ans+=1
                return ans
            elif queue[0][1]-1==0:
                ans+=1
                queue.popleft()
            else:
                i,num=queue.popleft()
                queue.append([i,num-1])
                ans+=1
            


        