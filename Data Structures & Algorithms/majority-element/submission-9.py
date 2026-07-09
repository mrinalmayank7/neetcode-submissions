class Solution:
  # boyer moore  voting
    def majorityElement(self, nums: List[int]) -> int:
      candidate, count = nums[0], 0
      for num in nums:
        if num == candidate:
          count +=1
        else:
          count -=1
          if count == 0:
            candidate = num
            count = 1
        #print("candidate ",candidate)
      return candidate

    def majorityElementHashmap(self, nums: List[int]) -> int:
      hashmap = dict.fromkeys(nums,0)
      for num in nums:
        hashmap[num] +=1
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
Approach 1 — Sort + Scan:
Idea: sort → count consecutive frequency → return element with max frequency
Time: O(n log n), Space: O(1)

Approach 2 — HashMap:
Idea: store element as key, frequency as value → return key with max value
Time: O(n), Space: O(n)

Approach 3 — Boyer-Moore Voting:
Idea: treat majority as election → candidate gains vote when matched, loses vote when different element found → majority always survives cancellation → return final candidate
Time: O(n), Space: O(1)
Why n/2 only: majority appears >n/2 times → has more votes than ALL others combined → mathematically impossible to fully cancel → any element appearing ≤n/2 times can be cancelled → Boyer-Moore breaks

"""
