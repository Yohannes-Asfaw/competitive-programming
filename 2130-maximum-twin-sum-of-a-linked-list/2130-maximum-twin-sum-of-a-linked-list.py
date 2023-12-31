# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast,mid=head,head
        while fast and fast.next: 
            fast=fast.next.next
            mid=mid.next
        node=None

        while mid:  
            tmp=mid.next
            mid.next=node
            node=mid
            mid=tmp

        res=0
        while node:
            res=max(res,(node.val+head.val))
            node=node.next
            head=head.next
        return res