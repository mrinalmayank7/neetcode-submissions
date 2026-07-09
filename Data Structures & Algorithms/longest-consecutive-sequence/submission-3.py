class Solution:
  def longestConsecutive(self, nums: List[int]) -> int:
    numset= set(nums)
    max_sequence=0
    while len(numset)>0:
      num = next(iter(numset))
      numset.remove(num)
      counter, left, right = 1,num-1,num+1

      while left in numset:
        numset.remove(left)
        counter +=1
        left = left-1

      while right in numset:
        numset.remove(right)
        counter+=1
        right = right +1
      max_sequence = max(max_sequence, counter)
    return max_sequence


    def longestConsecutiveBrute(self, nums: List[int]) -> int:
      nums.sort()
      if len(nums) ==0:
        return 0
      if len(nums) == 1:
        return 1
      current_max = 0
      current_counter = 1
      for i in range(len(nums)-1):
        if (nums[i+1]-nums[i] == 1):
          current_counter +=1
        elif (nums[i+1]-nums[i] > 1):
          current_max = max(current_max,current_counter)
          current_counter = 1
        else:
          continue

      current_max = max(current_max,current_counter)
      return current_max




