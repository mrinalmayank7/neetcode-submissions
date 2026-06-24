class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        arr=nums
        slow = 0
        fast = 0
        while fast < len(arr):
            if arr[fast] != val:
                arr[slow] = arr[fast]
                slow += 1
            fast += 1
        del arr[slow:]
        return slow

"""
nums = [3, 2, 2, 3]  val = 3  k = 0

num=3 → its val,  SKIP,  nums=[3, 2, 2, 3]  k=0
num=2 → not val,  WRITE, nums=[2, 2, 2, 3]  k=1
num=2 → not val,  WRITE, nums=[2, 2, 2, 3]  k=2
num=3 → its val,  SKIP,  nums=[2, 2, 2, 3]  k=2

return 2 
first k=2 elements → [2, 2] 
"""      