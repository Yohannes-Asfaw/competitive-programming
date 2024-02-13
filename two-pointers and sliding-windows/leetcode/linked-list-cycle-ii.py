# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s=set()
        dummy=head
        while dummy:
            if dummy in s:
                return dummy
            s.add(dummy)
            dummy=dummy.next
            
        return None