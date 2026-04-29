"""
 OOD: No
 Constraints: No
 input : List[List[int]], int
 output :  List[List[int]]
"""
# Keyword: Top K elements -> Max/Min Heap
# Image :build a heap that only holds K spots traverse the array, and the weakest/biggest ones get kicked out the top, where new elements "bubble" into place
from typing import List
import heapq
class Solution:
  def kClosest(self, points: List[List[int]], k:int) -> List[List[int]]:
    maxHeap = []
    for point in points:
      x, y = point[0], point[1]
      distance = x**2 + y**2
      heapq.heappush(maxHeap,(-distance,x,y))
      if len(maxHeap)>k:
        heapq.heappop(maxHeap)
    res = []
    while maxHeap:
      distance,x,y = heapq.heappop(maxHeap)
      res.append([x,y])
    return res
def test():
  sol = Solution()
  points = [[0,2],[2,0],[2,2]]
  result = sol.kClosest(points,2)
  print(f"result: {result}")

if __name__ == "__main__":
    test()

# Time Complexity: O(N log K)
  # We process N points, and each heap operation takes log K time. O(NlogK)
  # while maxHeap : O(KlogK)
# Space complexut : O(K)
  # Create siez K heap















