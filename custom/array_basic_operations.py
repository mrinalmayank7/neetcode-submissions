arr = [10, 20, 20, 30, 20, 40]
print("Original:", arr)

# insert at end — O(1)
arr.append(50)
print("Insert end (50):", arr)

# insert at middle — O(n)
arr.insert(2, 99)
print("Insert at index 2 (99):", arr)

# delete at end — O(1)
arr.pop()
print("Delete end:", arr)

# delete by index — O(n)
arr.pop(2)
print("Delete index 2:", arr)

# delete by value brute — O(n²)
def delete_value_brute(arr, val):
    i = 0
    while i < len(arr):
        if arr[i] == val:
            for j in range(i, len(arr) - 1):
                arr[j] = arr[j + 1]
            arr.pop()
        else:
            i += 1
    return arr

# delete by value optimal two pointer — O(n)
def delete_value_optimal(arr, val):
    slow = 0
    fast = 0
    while fast < len(arr):
        if arr[fast] != val:
            arr[slow] = arr[fast]
            slow += 1
        fast += 1
    del arr[slow:]
    return arr

arr1 = [10, 20, 20, 30, 20, 40]
arr2 = [10, 20, 20, 30, 20, 40]
print("Delete val 20 brute:", delete_value_brute(arr1, 20))
print("Delete val 20 optimal:", delete_value_optimal(arr2, 20))



"""
# [10,20,20,30,20,40], val=20
# trace:
# fast=0: arr[0]=10 ≠ 20 → arr[slow=0]=10, slow=1
# fast=1: arr[1]=20 = 20 → SKIP, slow stays 1
# fast=2: arr[2]=20 = 20 → SKIP, slow stays 1
# fast=3: arr[3]=30 ≠ 20 → arr[slow=1]=30, slow=2
# fast=4: arr[4]=20 = 20 → SKIP, slow stays 2
# fast=5: arr[5]=40 ≠ 20 → arr[slow=2]=40, slow=3
# del arr[3:] → removes leftover
# [10,30,40] O(n)!
"""
