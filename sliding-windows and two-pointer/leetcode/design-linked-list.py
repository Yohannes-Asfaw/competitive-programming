class Node:
    def __init__(self,val,n=None):
        self.val=val
        self.next=n

class MyLinkedList:
    
    def __init__(self):
        self.head=None
        self.size=0
        

    def get(self, index: int) -> int:
        if (index>=self.size):
            return -1
        temp=self.head
        while index>0:
            temp=temp.next
            index-=1
        return temp.val

        
        

    def addAtHead(self, val: int) -> None:
        if self.head==None:
            self.head=Node(val)
        else:
            self.head = Node(val, self.head)

        self.size+=1

        

    def addAtTail(self, val: int) -> None:
        if self.head==None:
            self.head=Node(val)
        else:
            temp=self.head
            while temp.next:
                temp=temp.next

            temp.next=Node(val)
        self.size+=1
        

    def addAtIndex(self, index: int, val: int) -> None:
        
        if index<0 or index>self.size:
            return
        if index==0:
            self.addAtHead(val)
        else:
            curr = self.head
            while(index > 1):
                index -= 1
                curr = curr.next
            curr.next = Node(val, curr.next)
        self.size+=1


        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        if index == 0:
            self.head = self.head.next
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
    
            temp.next = temp.next.next
        self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)