# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        curr=head.next
        rev=head
        rev.next=None
        while curr:
            temp=curr.next
            curr.next=rev
            rev=curr
            curr=temp
        return rev
            
        