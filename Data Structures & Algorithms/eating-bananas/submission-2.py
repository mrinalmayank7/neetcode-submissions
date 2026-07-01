import math

class Solution:
    def findpilehours(self,piles,k):
        hours=0
        for pile in piles:
            hours = hours + math.ceil(pile/k)
        return hours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        TC= O(n log(max(piles))), SC= O(1)
        """
        low =1
        high = max(piles)
        while low <= high:
            mid = (low+high)//2
            hours= self.findpilehours(piles, mid)
            if hours <= h:        # works (includes == and <)
                high = mid - 1    # try smaller — don't return here!
            else:                 # too slow
                low = mid + 1

        return low #valid min speed if mid not valid
"""
BRUTE: TC = O (MAX(PILES) * N), SC = O(1)
class Solution:
    def findpilehours(self,piles,k):
        hours=0
        for pile in piles:
            hours = hours + math.ceil(pile/k)
        return hours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = max(piles)
        for i in range(1,k+1):
            hours=self.findpilehours(piles,i)
            if hours <= h:
                return i
        return -1
"""
        

            
            


