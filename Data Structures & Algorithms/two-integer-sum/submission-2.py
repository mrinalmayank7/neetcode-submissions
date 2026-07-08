class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      hashmap={}
      for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap:
          return[hashmap[complement],i]
        else:
          hashmap[nums[i]]= i
      return []
        
    def twoSumBrute(self, nums: List[int], target: int) -> List[int]:
      for i in range(len(nums)):
        for j in range(i+1,len(nums)):
          if nums[i] + nums[j] == target:
            return [i,j]
      return []


"""
Brute: two nested loops, try every pair → O(n²) time O(1) space
Optimal: HashMap — store each number, check if complement exists → O(n) time O(n) space

Optimal:
For every number x — you need target-x to exist in array.
HashMap stores numbers seen so far → O(1) lookup for target-x → O(n) total.


nums=[2,7,11,15], target=9
HashMap={}

i=0, x=2: target-x=7, 7 in HashMap? NO → store {2:0}
i=1, x=7: target-x=2, 2 in HashMap? YES → return [0,1] ANSWER

TC/SC:
Brute: O(n²) time O(1) space
Optimal: O(n) time O(n) space
Natural fit: HashMap pattern 1 — lookup/existence

"""
