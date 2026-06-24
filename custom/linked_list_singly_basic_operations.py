"""
LINKED LIST — Complete Operations
Time and Space for each operation explained inside

NODE STRUCTURE:
[val | next] → [val | next] → [val | next] → None
  ↑                                            ↑
 head                                        last node always points to None
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val  = val   # stores the data
        self.next = next  # pointer to next node, default None


# ─────────────────────────────────────────────
# CREATE LIST: 10 → 20 → 30 → 40 → 50 → None
# ─────────────────────────────────────────────
head = ListNode(10)
head.next = ListNode(20)
head.next.next = ListNode(30)
head.next.next.next = ListNode(40)
head.next.next.next.next = ListNode(50)


# ─────────────────────────────────────────────
# INSERT AT BEGINNING
# Time:  O(1) — no traversal, just pointer changes
# Space: O(1) — only one new node created
# ─────────────────────────────────────────────
def insert_beg(head, val):
    newnode = ListNode(val)

    newnode.next = head  # new node points to old head
    head = newnode       # head now points to new node

    # WHY no "not head" check?
    # even if list is empty (head=None)
    # newnode.next = None is perfectly fine!
    # new node becomes the only node

    return head  # always return head — caller must update it


# ─────────────────────────────────────────────
# INSERT AT END
# Time:  O(n) — must traverse whole list to find last node
# Space: O(1) — only one new node created
# ─────────────────────────────────────────────
def insert_end(head, val):
    newnode = ListNode(val)

    # PRE-CHECK: if list is empty, new node IS the list
    # WHY? if head is None, cur=None, cur.next → CRASH!
    # so we handle empty list BEFORE the loop
    if not head:
        return newnode

    cur = head
    while cur.next:       # WHY cur.next not cur?
        cur = cur.next    # we need cur.next = newnode AFTER loop
                          # if we use "while cur", cur becomes None
                          # then None.next = newnode → CRASH!

    cur.next = newnode    # last node now points to new node
    return head


# ─────────────────────────────────────────────
# INSERT AT POSITION (0-indexed)
# Time:  O(n) — traverse to pos-1 in worst case
# Space: O(1) — only one new node created
# ─────────────────────────────────────────────
def insert_pos(head, val, pos):

    # PRE-CHECK: pos=0 means insert at beginning
    # WHY handle separately? insert_beg already written!
    # reuse code instead of duplicating logic
    if pos == 0:
        return insert_beg(head, val)

    newnode = ListNode(val)

    # PRE-CHECK: if list is empty, new node IS the list
    # WHY? cur=None, cur.next → CRASH inside loop
    if not head:
        return newnode

    cur = head
    for i in range(pos - 1):   # WHY pos-1?
                                # we want node BEFORE insertion point
                                # so we can do cur.next = newnode
                                # example: insert at pos=3 → stop at pos=2

        # GUARD: pos is beyond list length
        # WHY? if list has 3 nodes and pos=10
        # cur.next becomes None, cur=None → CRASH on next iteration
        if not cur.next:
            break               # stop at last node, insert at end
        cur = cur.next

    newnode.next = cur.next  # new node points to node after cur
    cur.next = newnode       # cur now points to new node

    # VISUAL:
    # before: cur → next_node
    # after:  cur → newnode → next_node

    return head


# ─────────────────────────────────────────────
# DELETE AT BEGINNING
# Time:  O(1) — just move head forward
# Space: O(1) — no extra space needed
# ─────────────────────────────────────────────
def delete_beg(head):

    # PRE-CHECK: empty list — nothing to delete
    # WHY? head.next on None → CRASH
    if not head:
        return None

    head = head.next  # head jumps to second node
                      # old head becomes garbage (Python GC cleans it)
    return head


# ─────────────────────────────────────────────
# DELETE AT END
# Time:  O(n) — must traverse to second last node
# Space: O(1) — no extra space needed
# ─────────────────────────────────────────────
def delete_end(head):

    # PRE-CHECK 1: empty list — nothing to delete
    # WHY? cur.next.next on None → CRASH
    if not head:
        return None

    # PRE-CHECK 2: only ONE node in list
    # WHY? if only 1 node, head.next = None
    # inside loop: cur.next.next = None.next → CRASH!
    # so we handle single node BEFORE the loop
    if not head.next:
        return None           # delete the only node → empty list

    cur = head
    while cur.next.next:      # WHY cur.next.next?
        cur = cur.next        # we want to STOP at second last node
                              # so we can do cur.next = None
                              # cur.next.next = None means
                              # cur.next IS the last node
                              # so cur is second last → STOP!

    cur.next = None           # cut off last node
    return head


# ─────────────────────────────────────────────
# DELETE AT POSITION (0-indexed)
# Time:  O(n) — traverse to pos-1 in worst case
# Space: O(1) — no extra space needed
# ─────────────────────────────────────────────
def delete_pos(head, pos):

    # PRE-CHECK: pos=0 means delete beginning
    # WHY handle separately? delete_beg already written!
    # reuse code instead of duplicating logic
    if pos == 0:
        return delete_beg(head)

    # PRE-CHECK: empty list — nothing to delete
    # WHY after pos==0? pos=0 on empty list
    # already handled by delete_beg above
    if not head:
        return None

    cur = head
    for i in range(pos - 1):  # WHY pos-1?
                               # stop at node BEFORE target
                               # so we can do cur.next = cur.next.next
                               # (skip the target node)

        # GUARD: pos is beyond list length
        # WHY? if list has 3 nodes and pos=10
        # cur becomes None → CRASH on next iteration
        if not cur.next:
            break              # stop, pos doesn't exist
        cur = cur.next

    # GUARD: make sure target node exists before skipping
    # WHY? if pos was out of range and we broke early
    # cur.next could be None → None.next → CRASH!
    if cur.next:
        cur.next = cur.next.next  # skip target node!

    # VISUAL of skip trick:
    # before: cur → target → next_node
    # after:  cur → next_node (target removed!)

    return head


# ─────────────────────────────────────────────
# TRAVERSE — print all nodes
# Time:  O(n) — visit every node once
# Space: O(1) — no extra space needed
# ─────────────────────────────────────────────
def traverse(head):
    cur = head
    while cur:            # WHY cur not cur.next?
        print(cur.val)    # we print cur.val inside loop
        cur = cur.next    # if we use cur.next, last node is MISSED!
                          # cur=None stops the loop safely


# ─────────────────────────────────────────────
# TEST
# ─────────────────────────────────────────────
# head = insert_beg(head, 200)   # 200→10→20→30→40→50
# head = insert_end(head, 500)   # 10→20→30→40→50→500
head   = insert_pos(head, 700, 4)  # 10→20→30→40→700→50
# head = delete_beg(head)        # 20→30→40→50
# head = delete_end(head)        # 10→20→30→40
# head = delete_pos(head, 5)     # deletes node at index 5

traverse(head)
