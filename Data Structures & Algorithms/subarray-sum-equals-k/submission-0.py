
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap=defaultdict(int)
        hashmap[0]=1
        count, prefix_sum=0,0
        for num in nums:
            prefix_sum +=num
            if prefix_sum - k in hashmap:
                count +=hashmap[prefix_sum - k]
            hashmap[prefix_sum] +=1
        
        return count

    def subarraySumBrute(self, nums: List[int], k: int) -> int:
        n=len(nums)
        count=0
        for i in range(n):
            total=0
            for j in range(i,n):
                total = total + nums[j]
                if total == k:
                    count +=1

        return count


"""

BRUTE — O(n²) time O(1) space:
Try every subarray starting at i, expand to j, check if sum==k.

```
nums=[1,2,3], k=3

i=0: [1]=1, [1,2]=3 ✅, [1,2,3]=6
i=1: [2]=2, [2,3]=5
i=2: [3]=3 ✅
count=2 ✅

*OPTIMAL — O(n) time O(n) space:**

Formula:

sum(L to R) = prefix[R] - prefix[L-1] = k
→ prefix[L-1] = prefix[R] - k


At every index R — check if (prefix_sum - k) exists as a PAST prefix sum → that many valid subarrays end at R.

Why same variable works as both L-1 and R:

when we ADD prefix_sum to HashMap → storing it as future L-1
when we CHECK prefix_sum-k        → using current sum as R, looking for matching L-1
same variable, two roles, separated by time


Why {0:1} initialized:

Prefix sum 0 exists before array starts (index -1). Needed when subarray starts from index 0 and sums to k — prefix[R]-k=0 must be found.


Trace:

nums=[1,2,3], k=3
hashmap={0:1}, prefix_sum=0, count=0

i=0: prefix_sum=1, check 1-3=-2? NO,  hashmap={0:1,1:1}
i=1: prefix_sum=3, check 3-3=0? YES freq=1 → count=1, hashmap={0:1,1:1,3:1}
i=2: prefix_sum=6, check 6-3=3? YES freq=1 → count=2, hashmap={0:1,1:1,3:1,6:1}
answer=2 

Frequency trace:

nums=[1,1,1], k=2
hashmap={0:1}, prefix_sum=0, count=0

i=0: prefix_sum=1, check -1? NO,  hashmap={0:1,1:1}
i=1: prefix_sum=2, check 0? YES freq=1 → count=1, hashmap={0:1,1:1,2:1}
i=2: prefix_sum=3, check 1? YES freq=1 → count=2, hashmap={0:1,1:1,2:1,3:1}
answer=2 

Tradeoffs:
Brute:   O(n²) time O(1) space → simple, try all subarrays
Optimal: O(n)  time O(n) space → prefix+HashMap, one pass
         trades space for time
         frequency handles multiple valid starting points
"""