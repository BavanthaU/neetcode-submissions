import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        out = []
        for x,y in points:
            distance_sq = x*x + y*y
            heapq.heappush(h, (distance_sq, (x,y)))
        
        print(h)
        i=0
        while i < k:
            closest, coordinate = heapq.heappop(h)
            out.append(coordinate)
            i+=1
        return out