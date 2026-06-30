# ============================================================
# MERGE SORT — ARRAY vs LINKED LIST
# ============================================================
# PROBLEM: Sort elements in ascending order
#
# WHY MERGE SORT?
# Array     → quicksort preferred but merge sort also works
# LinkedList → merge sort ONLY, no random access for quicksort
#
# ALGORITHM — 3 steps same for both:
# 1. FIND MID  → split into two halves
# 2. RECURSE   → sort left, sort right
# 3. MERGE     → combine two sorted halves
#
# RECURRENCE RELATION:
# T(n) = 2T(n/2) + O(n)
#         ↑          ↑
#   2 halves    merge step
#
# MASTERS THEOREM:
# T(n) = aT(n/b) + f(n)
# here: a=2, b=2, f(n)=n
# log_b(a) = log_2(2) = 1
# f(n) = n = n^1 = n^log_b(a)
# → CASE 2 of masters theorem
# → T(n) = O(n logn)
#
# LEVELS VISUAL:
# Level 0: 1 array  of n    → n work
# Level 1: 2 arrays of n/2  → n work
# Level 2: 4 arrays of n/4  → n work
# logn levels × n work = O(n logn)
# ============================================================


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val  = val
        self.next = next


# ============================================================
# ARRAY MERGE SORT
# ============================================================
# TC: O(n logn) — logn levels, n merge work each level
# SC: O(n)      — extra arrays created at each merge step
#                 unlike LL which reuses existing nodes
# ============================================================

def merge_arr(left, right):
    # WHY dummy result array?
    # need somewhere to collect sorted elements
    # arrays cant reuse nodes like LL does
    result = []
    i, j   = 0, 0

    # compare left[i] and right[j]
    # take smaller, advance that pointer
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # one side exhausted — attach remaining directly
    # remaining is already sorted, no need to compare
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort_arr(arr):
    # base case: 0 or 1 element already sorted
    if len(arr) <= 1:
        return arr

    # FIND MID
    # WHY len(arr)//2?
    # array has direct index access O(1)
    # no traversal needed unlike LL
    mid   = len(arr) // 2
    left  = merge_sort_arr(arr[:mid])   # sort left half
    right = merge_sort_arr(arr[mid:])   # sort right half

    # merge two sorted halves
    return merge_arr(left, right)


# ============================================================
# LINKED LIST MERGE SORT
# ============================================================
# TC: O(n logn) — same recurrence T(n)=2T(n/2)+O(n)
# SC: O(logn)   — only call stack depth
#                 NO extra arrays — reuse existing nodes
#                 this is the key advantage over array sort
# ============================================================

def find_mid(head):
    # WHY slow/fast pointer?
    # LL has no len(), no index
    # cant do mid = len//2 directly
    # must physically walk to middle
    # fast moves 2x → when fast ends, slow is at mid
    slow = head
    fast = head

    # WHY fast.next and fast.next.next
    # NOT fast and fast.next?
    #
    # fast and fast.next → slow goes too far
    # 4→1→3→2:
    #   slow=1,fast=3 → slow=3,fast=None
    #   mid=3 → left=4→1→3, right=2 UNEVEN ❌
    #
    # fast.next and fast.next.next → even split
    # 4→1→3→2:
    #   slow=1,fast=3
    #   fast.next=2, fast.next.next=None → STOP
    #   mid=1 → left=4→1, right=3→2 EVEN ✅
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def merge_ll(left, right):
    # WHY dummy node?
    # result head could be from left or right
    # dummy gives fixed anchor, no special head case
    # return dummy.next = real sorted head
    dummy = ListNode(0)
    cur   = dummy

    while left and right:
        if left.val <= right.val:
            cur.next = left       # attach smaller node
            left     = left.next  # advance left pointer
        else:
            cur.next = right
            right    = right.next
        cur = cur.next            # WHY? cur must move forward
                                  # without this overwrites same node

    # attach remaining — already sorted
    cur.next = left if left else right
    return dummy.next


def merge_sort_ll(head):
    # base case: 0 or 1 node already sorted
    if not head or not head.next:
        return head

    # FIND MID and CUT
    mid        = find_mid(head)
    right_head = mid.next    # save right half start
    mid.next   = None        # WHY cut?
                             # WITHOUT: 4→1→3→2 left still
                             # connected to right
                             # sortList never hits base case
                             # → infinite loop ❌
                             # WITH: 4→1→None and 3→2→None
                             # physically separate → works ✅

    left  = merge_sort_ll(head)        # sort left half
    right = merge_sort_ll(right_head)  # sort right half

    return merge_ll(left, right)


# ============================================================
# HELPERS FOR LL TESTING
# ============================================================

def to_ll(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    cur  = head
    for val in arr[1:]:
        cur.next = ListNode(val)
        cur      = cur.next
    return head


def to_arr(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# ============================================================
# TEST CASES
# ============================================================

print("=== ARRAY MERGE SORT ===")
print(merge_sort_arr([4, 1, 3, 2]))      # [1,2,3,4]
print(merge_sort_arr([1, 2, 3, 4]))      # [1,2,3,4]
print(merge_sort_arr([4, 3, 2, 1]))      # [1,2,3,4]
print(merge_sort_arr([1]))               # [1]
print(merge_sort_arr([]))                # []
print(merge_sort_arr([-1, 5, 3, 4, 0])) # [-1,0,3,4,5]
print(merge_sort_arr([3, 1, 3, 2, 1]))  # [1,1,2,3,3]

print("\n=== LINKED LIST MERGE SORT ===")
print(to_arr(merge_sort_ll(to_ll([4, 1, 3, 2]))))      # [1,2,3,4]
print(to_arr(merge_sort_ll(to_ll([1, 2, 3, 4]))))      # [1,2,3,4]
print(to_arr(merge_sort_ll(to_ll([4, 3, 2, 1]))))      # [1,2,3,4]
print(to_arr(merge_sort_ll(to_ll([1]))))                # [1]
print(to_arr(merge_sort_ll(to_ll([]))))                 # []
print(to_arr(merge_sort_ll(to_ll([-1, 5, 3, 4, 0])))) # [-1,0,3,4,5]
print(to_arr(merge_sort_ll(to_ll([3, 1, 3, 2, 1]))))  # [1,1,2,3,3]


# ============================================================
# TRACE — [4,1,3,2]
# ============================================================
#
# DIVIDE (going down):
# merge_sort(4→1→3→2)
# ├── merge_sort(4→1)
# │   ├── merge_sort(4) → 4   ← base case
# │   └── merge_sort(1) → 1   ← base case
# └── merge_sort(3→2)
#     ├── merge_sort(3) → 3   ← base case
#     └── merge_sort(2) → 2   ← base case
#
# MERGE (coming up):
# merge(4,1):
#   1<4 → take 1, right=None
#   left=4 remains → cur.next=4
#   return 1→4
#
# merge(3,2):
#   2<3 → take 2, right=None
#   left=3 remains → cur.next=3
#   return 2→3
#
# merge(1→4, 2→3):
#   1<2 → take 1, left=4
#   2<4 → take 2, right=3
#   3<4 → take 3, right=None
#   left=4 remains → cur.next=4
#   return 1→2→3→4 
#
# ============================================================
# ARRAY vs LL COMPARISON
# ============================================================
#
#              ARRAY          LINKED LIST
# Find mid   → O(1) index    → O(n) slow/fast pointer
# Split      → arr[:mid]     → mid.next=None (manual cut)
# Merge      → new array     → reuse existing nodes
# TC         → O(n logn)     → O(n logn)
# SC         → O(n)          → O(logn) ← advantage
# ============================================================
