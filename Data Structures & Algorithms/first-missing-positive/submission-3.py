class Solution:
    #INDEX MARKING
    def firstMissingPositive(self, nums: List[int]) -> int:
      n = len(nums)
      for i in range(n):
        if nums[i] <=0 or nums[i]>n:
          nums[i] = n+1 #n+1 act as invalid 
      for i in range(n):
        cur = abs(nums[i])
        if 1<=cur<=n:
          if nums[cur-1] > 0:
            nums[cur-1] = - nums[cur-1]
      for i in range(n):
        if nums[i]>0:
          return i+1

      return n+1
    def firstMissingPositiveSorting(self, nums: List[int]) -> int:
      nums.sort()
      expected=1
      for num in nums:
        if num <=0:
          continue
        elif num == expected:
          expected +=1
        elif num > expected:
          return expected
      return expected

    def firstMissingPositiveHashmap(self, nums: List[int]) -> int:
      hashset=set(nums)
      for i in range(1,len(nums)+2): # if we have [1,2,3], we need to check 1,2,3 but answer is i=4, len(nums)=3 iterate from 1 to 2
        if i not in hashset:
          return i  


"""
3 approaches:
Approach 1: HashSet         → O(n) time O(n) space
Approach 2: Sort + scan     → O(n log n) time O(1) space
Approach 3: Index marking   → O(n) time O(1) space ← optimal

APPROACH 1 — HashSet
Core idea: Store all numbers in HashSet. Check 1,2,3... in order — first one missing = answer.
eg [1,2,3] , ans = 4, iterate i from 1 to 4 -> range(1, len(n)+2)


APPROACH 2 — Sort + Scan
Core idea:
Sort array. Scan looking for first gap in positive sequence starting from 1.

Rules:
Rule A — sort array
Rule B — expected = 1
Rule C — for each num: if num == expected → expected++, skip duplicates and negatives
Rule D — return expected

Trace:
nums=[3,4,-1,1]
sorted=[-1,1,3,4]
expected=1

num=-1: negative → skip
num=1:  1==expected → expected=2
num=3:  3!=expected(2) → return 2 


APPROACH 3 — Index Marking 

Core idea: Use the array itself as a HashSet. Number x belongs at index x-1.
1 → index 0
2 → index 1
3 → index 2
...
n → index n-1

therefore we need to return index + 1 as answer, using indexes as storing positive values
Array: [3,4,-1,1], n=4

We have the array itself with 4 slots:
index:  0   1   2   3
value: [3,  4, -1,  1]
*Idea: what if each index REPRESENTS a number?

index 0 → represents number 1
index 1 → represents number 2
index 2 → represents number 3
index 3 → represents number 4

What signals can we use without losing value?

- We can't change the value itself — we still need it.
- But we can change its SIGN. Sign carries extra information

Now process [3,4,5,1]:
Process number 3:
3 is present in array. Index for 3 = 3-1 = 2.
Go to index 2, make it negative = "number 3 is present":

index:  0  1   2  3
value: [3, 4, -5, 1]
               ↑
               index 2 now negative = number 3 present

Process number 4:
4 is present. Index for 4 = 4-1 = 3.
value: [3, 4, -5, -1]

Process number 5:
5 > n=4 → irrelevant → skip.

Process number 1:
1 is present. Index for 1 = 1-1 = 0.
value: [-3, 4, -5, -1]
 

Now scan and find first positive index:
value: [-3, 4, -5, -1]
return 1+1 = 2 answer

""" 