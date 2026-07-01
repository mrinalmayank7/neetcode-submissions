# ============================================================
# BINARY SEARCH — ITERATIVE & RECURSIVE
# ============================================================
# RULES:
# RULE 1: arr[mid] == target → FOUND, return mid
# RULE 2: arr[mid] < target  → target in RIGHT half, discard LEFT  (low = mid+1)
# RULE 3: arr[mid] > target  → target in LEFT half,  discard RIGHT (high = mid-1)
#
# BASE CASE:
# Sorting  → low < high   (need 2+ elements to sort)
# Searching → low <= high  (need 1+ element to check, it could be target)
#
# TC: O(log n) — halves search space each step
# SC: O(1) iterative, O(log n) recursive (call stack)
# ============================================================


# ────────────────────────────────────────────
# ITERATIVE
# ────────────────────────────────────────────
def binarySearchIterative(arr, target):
    low  = 0
    high = len(arr) - 1

    while low <= high:              # search space exists (at least 1 element)
        mid = (low + high) // 2

        if arr[mid] == target:      # RULE 1: found
            return mid
        elif arr[mid] < target:     # RULE 2: go right
            low = mid + 1
        else:                       # RULE 3: go left
            high = mid - 1

    return -1                       # search space exhausted, not found


# ────────────────────────────────────────────
# RECURSIVE (same style as quickSort)
# ────────────────────────────────────────────
def binarySearchRecursive(arr, target, low, high):
    if low <= high:                 # search space exists (same condition as iterative)
        mid = (low + high) // 2

        if arr[mid] == target:      # RULE 1: found
            return mid
        elif arr[mid] < target:     # RULE 2: go right
            return binarySearchRecursive(arr, target, mid + 1, high)
        else:                       # RULE 3: go left
            return binarySearchRecursive(arr, target, low, mid - 1)

    return -1                       # search space exhausted, not found


# ============================================================
# TRACE — arr=[1,3,5,7,9,11,13,15], target=11
# ============================================================
#
# low=0, high=7
#
# STEP 1:
#   mid = (0+7)//2 = 3
#   arr[3] = 7
#   11 > 7 → RULE 2: go right
#   low = 4
#
# STEP 2:
#   low=4, high=7
#   mid = (4+7)//2 = 5
#   arr[5] = 11
#   11 == 11 → RULE 1: FOUND
#   return 5 
#
# ────────────────────────────────────────────
# TRACE — target=6 (not in array)
# ────────────────────────────────────────────
#
# low=0, high=7
#
# STEP 1:
#   mid = (0+7)//2 = 3
#   arr[3] = 7
#   6 < 7 → RULE 3: go left
#   high = 2
#
# STEP 2:
#   low=0, high=2
#   mid = (0+2)//2 = 1
#   arr[1] = 3
#   6 > 3 → RULE 2: go right
#   low = 2
#
# STEP 3:
#   low=2, high=2
#   mid = (2+2)//2 = 2
#   arr[2] = 5
#   6 > 5 → RULE 2: go right
#   low = 3
#
# STEP 4:
#   low=3 > high=2 → low <= high FAILS
#   return -1 (not found)
#
# ============================================================
# TEST
# ============================================================
arr = [1,3,5,7,9,11,13,15]
