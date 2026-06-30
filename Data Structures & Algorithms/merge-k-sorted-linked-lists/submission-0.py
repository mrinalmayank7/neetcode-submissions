# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution: 
    def merge (self,list1,list2):
        dummy = ListNode(0) 
        cur=dummy
        while list1 and list2:
            if list1.val <= list2.val:
                cur.next=list1
                list1=list1.next
            else:
                cur.next=list2
                list2=list2.next
            cur=cur.next
        cur.next = list1 if list1 else list2
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:                    # empty input
                return None
        if len(lists) == 1:
            return lists[0]

        #OPTIMAL
        mid = len(lists)//2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        return self.merge(left,right)
        #BRUITE FORCE

        #result = lists[0]
        #for i in range (1,len(lists)):
        #    result = self.merge(result,lists[i])
        #return result
    

    