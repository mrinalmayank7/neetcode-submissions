class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
      nums.sort()
      if len(nums) ==0:
        return 0
      if len(nums) == 1:
        return 1
      current_max = 0
      current_counter = 1
      for i in range(len(nums)-1):
        if (nums[i+1]-nums[i] == 1):
          print ("INCREMENTED")
          current_counter +=1
        if (nums[i+1]-nums[i] > 1):
          print ("SET TO 0")
          current_max = max(current_max,current_counter)
          current_counter = 1
        print(current_counter)
        current_max = max(current_max,current_counter)
      return current_max





      return current_max