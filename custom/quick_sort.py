
# QUICK SORT
# Strategy: PARTITION first (real work), THEN recurse
# Modifies SAME array in-place, no new arrays created

def quickSort(arr, low, high):
    # base case: 0 or 1 element in this range, already sorted
    if low < high:
        # PARTITION — real work happens HERE, before recursing
        pivot_index = partition(arr, low, high)

        # recurse on LEFT portion of SAME array
        quickSort(arr, low, pivot_index - 1)

        # recurse on RIGHT portion of SAME array
        quickSort(arr, pivot_index + 1, high)


def partition(arr, low, high):
    pivot = arr[high]   # choose last element as pivot
    i = low              # next empty slot for "smaller than pivot"

    for j in range(low, high):
        if arr[j] < pivot:
            # swap arr[j] into the "smaller" zone
            arr[i], arr[j] = arr[j], arr[i]
            i += 1        # advance the empty slot

    # place pivot in its correct final sorted position
    arr[i], arr[high] = arr[high], arr[i]

    return i   # pivot's final index, used to split recursion


# ============================================================
# USAGE
# ============================================================


arr2 = [20, 2, 7, 12, 15, 1, 6, 8]
quickSort(arr2, 0, len(arr2) - 1)
print(arr2)               # [1, 2, 6, 7, 8, 12, 15, 20]




# ============================================================
# TRACE — QUICK SORT on [20,2,7,12,15,1,6,8]
# ============================================================
#
# quickSort(arr, 0, 7)
#   partition(arr, 0, 7), pivot=8
#     → arr becomes [2,7,1,6,8,20,12,15]
#     → pivot_index=4
#   quickSort(arr, 0, 3)        LEFT  [2,7,1,6]
#     partition(arr, 0, 3), pivot=6
#       → arr becomes [2,1,6,7]  (within this range)
#       → pivot_index=2
#     quickSort(arr, 0, 1)      LEFT  [2,1]
#       partition pivot=1 → [1,2], pivot_index=0
#       quickSort(arr, 0, -1)   base case
#       quickSort(arr, 1, 1)    base case
#     quickSort(arr, 3, 3)      RIGHT base case
#   quickSort(arr, 5, 7)        RIGHT [20,12,15]
#     partition(arr, 5, 7), pivot=15
#       → arr becomes [12,15,20] (within this range)
#       → pivot_index=6
#     quickSort(arr, 5, 5)      LEFT  base case
#     quickSort(arr, 7, 7)      RIGHT base case
#
# Final: [1,2,6,7,8,12,15,20] 
#
#
# ============================================================
# TRADEOFFS — MERGE SORT vs QUICK SORT
# ============================================================
#
#                    MERGE SORT          QUICK SORT
# Work happens     → AFTER recursion    BEFORE recursion
#                    (bottom-up)         (top-down)
#
# Array handling   → creates NEW         modifies SAME
#                    arrays each merge   array in-place
#
# Time (best/avg)  → O(n logn)           O(n logn)
# Time (worst)     → O(n logn) GUARANTEED → O(n²) possible
#                    (always balanced)    (unbalanced pivot)
#
# Space            → O(n)                O(logn) avg
#                    (new arrays)         O(n) worst
#                                         (just recursion stack,
#                                          no new arrays)
#
# Stability        → STABLE              NOT stable
#                    (equal elements      (swaps can reorder
#                     keep relative        equal elements)
#                     order)
#
# Best use case    → Linked Lists         Arrays
#                    (no random access     (needs arr[pivot]
#                     needed, sequential    direct access)
#                     merge works great)
#
# Predictability   → ALWAYS O(n logn)     worst case O(n²)
#                    regardless of input   on sorted/reverse
#                                          sorted input
#                                          (fixable with
#                                           random pivot)
# ============================================================
