class Solution:
    def majorityElement(self, nums: List[int]) -> int:
      hashmap = dict.fromkeys(nums,0)
      for num in nums:
        hashmap[num] +=1
      print(hashmap)
      return max(hashmap, key=hashmap.get) 

    def majorityElementBrute(self, nums: List[int]) -> int:
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


"""
Approach 1 — Sort + Scan (brute):
Time: O(n log n) — sort dominates
Space: O(1) — no extra space
How: sort → scan → track frequency of consecutive elements → return element with max frequency

Approach 2 — HashMap Count:
Time: O(n)
Space: O(n) — HashMap stores all unique elements

"""
