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

"""

Input:  [100,4,200,1,3,2]
Output: 4  (sequence 1,2,3,4)
APPROACH 1 — Brute: Sort + Scan

1. Sort array
2. scan left to right
   - track current consecutive sequence length 
   - update max when sequence breaks.

Why sorting works:

After sorting, consecutive numbers are adjacent. 
Just scan once and count. 
Simple but sorting costs O(n log n) — violates problem constraint.

Why skip duplicates:

Duplicate numbers are not consecutive, same number twice doesn't extend sequence. 
nums[i+1]-nums[i]==0 → skip, don't increment counter, don't reset.


Rules:
Rule A — sort array
Rule B — if empty → return 0, if single → return 1
Rule C — for each adjacent pair:
- diff==1 → consecutive → increment counter
- diff>1 → gap → update max, reset counter to 1
- diff==0 → duplicate → skip (continue)
Rule D — after loop → update max one final time (catches last sequence)


TC/SC — Brute:
Time: O(n log n) — sorting dominates
Space: O(1) — sort in place, no extra space


APPROACH 2 — Optimal: HashSet + Bidirectional Expansion

Core idea:

Store all numbers in HashSet for O(1) lookup. 
Pick any element:
- expand left (-1,-2...)
- expand right (+1,+2...) to find full sequence
- remove elements as you go 
- break if +1 or -1 not found


Why HashSet instead of array:

Array lookup = O(n) 
HashSet lookup = O(1) 
HashSet contains unique values

**Why remove elements while expanding:**

Without removal — same element could be picked again as starting point in outer loop 
With removal — once element processed, gone forever. Never counted twice. Guarantees each element contributes to exactly ONE sequence count.

Why O(n) even with nested while loops (IMP):
Each element removed exactly once across entire run. Total removals = n. 
Total iterations across ALL while loops combined = n. 
Not O(n) per outer iteration — O(n) total across all iterations.

Rules:
Rule A — convert array to HashSet (removes duplicates automatically)
Rule B — while set not empty → pick any element, remove it
Rule C — initialize counter=1, left=x-1, right=x+1
Rule D — left while: if left in set → remove, counter++, left--
Rule E — right while: if right in set → remove, counter++, right++
Rule F — update max → repeat


Optimal (HashSet):
  Time:  O(n)  ← each element once
  Space: O(n)  ← HashSet storage


"""


