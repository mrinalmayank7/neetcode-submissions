class Node:
    def __init__(self, val=0):
        self.val  = val
        self.prev = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None   

    def get(self, index: int) -> int:
        if index < 0:
            return -1
        cur = self.head
        i = 0
        while cur:
            if i == index:
                return cur.val
            i += 1
            cur = cur.next
        return -1     

    def addAtHead(self, val: int) -> None:
        newnode = Node(val)
        if not self.head:
            self.head = newnode
            self.tail = newnode
            return
        newnode.next = self.head
        self.head.prev=newnode
        self.head=newnode

    def addAtTail(self, val: int) -> None:
        newnode = Node(val)
        if not self.tail:
            self.tail = newnode
            self.head = newnode 
            return     
        newnode.prev = self.tail
        self.tail.next=newnode
        self.tail=newnode

    def addAtIndex(self, index: int, val: int) -> None:
        if index <=0:
            self.addAtHead(val)
            return
        cur=self.head
        i = 0
        #10(0),20(1),30(2), 40(3),   val=90, index = 2
        #i=0, cur = 10, 0!=1
        #i=1, cur=  20, 1==1, temp = 30,40 | 20 <-> 90
        while cur:
            if i  == index -1:
                newnode=Node(val)
                temp = cur.next
                cur.next = newnode
                newnode.prev = cur
                newnode.next = temp
                if temp:            # if temp exists (lastnode), update prev
                    temp.prev = newnode
                else:               # temp is None = inserting at tail
                    self.tail = newnode
                return
            i+=1
            cur=cur.next
        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or not self.head:
            return


        #10(0),20(1),30(2), 40(3),   index = 1
        #i=0, cur = 10, 0==0, 10 ->30
        cur=self.head
        i=0
        while cur:
            if i == index:
                if cur.prev:
                    cur.prev.next= cur.next
                else:
                    self.head= cur.next
                if cur.next:
                    cur.next.prev= cur.prev
                else:
                    self.tail=cur.prev
                return
                    
            i+=1
            cur=cur.next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)