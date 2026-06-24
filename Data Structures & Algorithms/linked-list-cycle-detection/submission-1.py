# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow == fast:
                return True
        return False
"""
TWO POINTER : OPTIMAL
time= O(N)
space = O(1)
"""  


"""
BRUTE FORCE
time= O(N)
space = O(N)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen=set()
        cur= head
        while cur:
            if cur in seen:
                return True
            seen.add(cur) 
            cur = cur.next
        return False
"""