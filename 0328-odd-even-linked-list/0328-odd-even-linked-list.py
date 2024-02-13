# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd=head
        even=ListNode(None)
        even1=even
        while odd and odd.next and even:
            temp=odd.next
            odd.next=odd.next.next
            if odd.next:
                odd=odd.next
            even.next=temp
            even=even.next
        even.next=None
        if odd and even1:
            odd.next=even1.next

        return head
            
            
        