def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        
        while head:
            front=head.next
            head.next=prev
            prev=head
            head=front

            
        return prev
