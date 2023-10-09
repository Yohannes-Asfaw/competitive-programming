def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        dummy=head
        curr =dummy.next
        
        while dummy and curr:
            if dummy.val==curr.val:
                curr=curr.next
                dummy.next=curr
            else:
                dummy=dummy.next
                curr=curr.next
            
        return head
