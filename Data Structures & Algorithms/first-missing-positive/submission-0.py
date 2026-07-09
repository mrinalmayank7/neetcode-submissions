class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
      hashset=set(nums)
      for i in range(1,len(nums)+2): # if we have [1,2,3], we need to check 1,2,3 but answer is i=4, len(nums)=3 iterate from 1 to 2
        if i not in hashset:
          return i   