import math 
class Solution:
    # QUICKSELECT RULES:
    # RULE 1: pivot_index == k → STOP, first k points are answer
    # RULE 2: pivot_index <  k → discard LEFT,  recurse RIGHT
    # RULE 3: pivot_index >  k → discard RIGHT, recurse LEFT
    #
    # ONLY DIFFERENCE FROM QUICKSORT:
    # partition  → compares DISTANCES not VALUES
    # quickSelect → recurses ONE side only, not both

    # Quickselect: O(n) avg,  O(n²) worst,  O(1) space
    def distance (self,point):
        return math.sqrt(point[0]**2 + point[1]**2)

    def partition(self, points, low, high):
        pivot = self.distance(points[high])
        i=low
        for j in range (low, high ):
            if self.distance(points[j]) < pivot:
                points[i],points[j]=points[j], points[i]
                i+=1
        points[i], points[high]= points[high], points[i]
        return i

    def quickselect(self,points, low, high,k):
        if low < high:
            pivot_index = self.partition(points,low,high)

            if pivot_index == k: #rule 1 (perfect elements in left)
                return
            if pivot_index < k: #rule 2 (less elements on left, search right)
                self.quickselect (points, pivot_index +1, high, k)
            if pivot_index > k: #rule 2 (too many elements on left)
                self.quickselect (points,low, pivot_index -1, k)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.quickselect(points,0,len(points)-1,k)
        return points[:k]

    """
    BRUTE FORCE: 
    TC: BEST & WORST: O (N LOG N)
    SPACE: O(N)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances=[]
        for point in points:
            dist = math.sqrt(point[0]**2 + point[1]**2)
            distances.append ((dist,point))
        distances.sort(key= lambda x : x[0])
        result = []
        for i in range(k):
            result.append(distances[i][1])
            
        return result
    """
        