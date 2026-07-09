class Solution:
    def majorityElement1(self, nums: List[int]) -> int:
      hashmap = dict.fromkeys(nums,0)
      for num in nums:
        hashmap[num] +=1
      print(hashmap)
      return max(hashmap, key=hashmap.get) 

    def majorityElement(self, nums: List[int]) -> int:
      nums.sort()
      max_freq = 0
      max_number=0
      counter = 0
      prev = nums[0]
      for i in  range(len(nums)):
        if nums[i] == prev:
          counter +=1
          prev = nums[i]
        else:
          if counter > max_freq:
            max_freq = counter
            max_number = prev
            counter = 1
        prev = nums[i]

      if counter > max_freq:
          max_freq = counter
          max_number = prev
      return max_number
