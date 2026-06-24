# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
   def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0)
    cur=dummy
    while list1 and list2:
        if list1.val < list2.val:
            cur.next=list1
            list1=list1.next
        else:
            cur.next=list2
            list2=list2.next
        cur=cur.next
    if list1:
        cur.next=list1
    else:
        cur.next=list2
    return dummy.next

"""
Time:  O(n+m)  
Space: O(1)    
"""
"""
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        a=[]
        cur=list1
        while cur:
            a.append(cur.val)
            cur=cur.next

        cur=list2
        while cur:
            a.append(cur.val)
            cur=cur.next
        a.sort()
        temp=ListNode(0) #first node is dummy
        cur=temp
        for x in a:
            cur.next = ListNode(x) #next to dummy add node
            cur=cur.next
        return temp.next #since first node is 0


time: x log x (sort) | x = m + n | o((n+m) log (n+m))
space: O(n+m)
"""

