def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new =new1= ListNode(None)
        
        while list1 and list2:
            if list1.val >list2.val:
                new.next=list2
                list2=list2.next
            else:
                new.next=list1
                list1=list1.next
            new=new.next
        new.next=list1 or list2
        return new1.next
