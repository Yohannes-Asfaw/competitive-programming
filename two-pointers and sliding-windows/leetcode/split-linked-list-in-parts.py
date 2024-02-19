# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        ans=[]
        dummy=head
        length=0
        while dummy:
            dummy=dummy.next
            length+=1
        curr_size = length // k
        reminder = length % k

        ans = []
        temp = head
        for i in range(k):
            ans.append(temp)
            updated_size = curr_size + 1 if reminder > 0 else curr_size
            reminder -= 1
            for j in range(updated_size - 1):
                temp = temp.next
            if temp:
                temp.next, temp = None, temp.next

        return ans

        