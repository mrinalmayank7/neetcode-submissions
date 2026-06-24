# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        cur=head
        while cur:
            next_node=cur.next
            cur.next=prev
            prev=cur
            cur = next_node
        return prev
        
"""
1,2,3,4
pass 1: 
cur=1, 
next_node = 2 (store)
cur.next (head) = prev (none)
prev= (head = 1)
curent=2
so initially prev is none (since head to point to none)
before moving to second loop change prev to current, and current to next
...
Time o(n), Space o(1)
"""