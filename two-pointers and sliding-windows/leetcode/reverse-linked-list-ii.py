# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr=head
        # going forward untile finding the left
        count=1
        while curr.next and count!=left:
            p=curr
            curr=curr.next
            count+=1
        if curr==head:
            firsthalf=None
        else:
            firsthalf=p

        
        start=curr
        prev=curr
        if curr:
            curr=curr.next    
        i=0
        if curr:
            temp=curr
        else:
            temp=None
        while curr and i<right-left:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
            i+=1
        if firsthalf==None:
            head=prev
        if curr:
            secondhalf=temp
        else:
            secondhalf=None 
        if firsthalf!=None: 
            firsthalf.next=prev
        if start:
            start.next=secondhalf
        if secondhalf==None and firsthalf==None:
            head=prev
        
        return head



            





        