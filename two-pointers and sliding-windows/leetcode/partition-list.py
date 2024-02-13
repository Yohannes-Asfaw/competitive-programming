# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy=head

        lessthan=ListNode(None)
        L=lessthan
        greaterthan=ListNode(None)
        G=greaterthan


        while dummy:
            if dummy.val>=x:
                greaterthan.next=dummy
                greaterthan=greaterthan.next
            elif dummy.val<x:
                lessthan.next=dummy
                lessthan=lessthan.next
            dummy=dummy.next
            greaterthan.next=None
            lessthan.next=None
            lessthan.next=G.next
        return L.next


        