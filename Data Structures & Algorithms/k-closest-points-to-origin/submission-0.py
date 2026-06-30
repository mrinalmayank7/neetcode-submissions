import math 
class Solution:
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
        