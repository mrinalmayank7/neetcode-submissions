class Solution:
    def majorityElement(self, nums: List[int]) -> int:
      if not nums:
        return 0
      hashmap = dict.fromkeys(nums,0)
      for num in nums:
        hashmap[num] +=1
      print(hashmap)
      return max(hashmap, key=hashmap.get)   