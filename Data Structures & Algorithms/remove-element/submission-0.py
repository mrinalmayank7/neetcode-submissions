class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for num in nums:
            if num != val:
                nums[k]=num
                k+=1
        return k

"""
nums = [3, 2, 2, 3]  val = 3  k = 0

num=3 → its val,  SKIP,  nums=[3, 2, 2, 3]  k=0
num=2 → not val,  WRITE, nums=[2, 2, 2, 3]  k=1
num=2 → not val,  WRITE, nums=[2, 2, 2, 3]  k=2
num=3 → its val,  SKIP,  nums=[2, 2, 2, 3]  k=2

return 2 
first k=2 elements → [2, 2] 
"""      