class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if not nums:
            return 0
        count = 0
        max_count=0

        for x in nums:
            if x == 1:
                count +=1
            else:
                max_count = max(count,max_count)
                count=0
        max_count = max(count,max_count)
        return max_count

"""
c=0,m=0
x=1, m=0, c=1
x=0, m =1,c=0
x=1, m=1, c=1
x=1, m=1, c=2
x=0, m=2, c=0
"""


        