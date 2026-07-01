import math

class Solution:
    def findpilehours(self,piles,k):
        hours=0
        for pile in piles:
            hours = hours + math.ceil(pile/k)
        return hours
    """
    CONDITION 1: hours ≤ h (mid is VALID)
    mid works! Koko CAN finish in time
    BUT we want MINIMUM speed
    there MIGHT be smaller valid speeds on LEFT
    → don't stop here
    → move high = mid - 1
        (shrink search space from right)
        (mid itself might be answer, but check left first)

    CONDITION 2: hours > h (mid is INVALID)
    mid is TOO SLOW, Koko CANNOT finish in time
    no point checking anything SLOWER (left of mid)
    all speeds left of mid are also invalid
    MUST go faster → go RIGHT
    → move low = mid + 1
        (shrink search space from left)
        (discard mid and everything left of it)
    """
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
        

            
            


