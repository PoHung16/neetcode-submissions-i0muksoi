"""
 OOD: No
 Constraints: No
 input : List[List[int]], int
 output :  List[List[int]]
"""
# Brute Force: 
    # Calculate the squared distance for every point, sort the entire array, and return the first k points.-> O(NlogN) 
class Solution:
  def kClosest(self, points: List[List[int]],k:int)->List[List[int]]:
    points.sort(key= lambda p: p[0]**2 + p[1]**2)
    return points[:k]

# Optimal Solution
    # Goal: O(NlogN)-> O(logN).. don't sort the whole array every time
    # Keyword: Bottom K elements -> Max Heap
    # Approach: Traverse an array and  build a heap that only holds K spots, then kick out the smallest one on the top,  where new elements "bubble" into place

from typing import List
import heapq
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k:int) -> List[List[int]]:
      maxheap = []
      for point in points:
        x, y = point[0], point[1]
        dist = x**2 + y**2
        heapq.heappush(maxheap,(-dist,x,y))
        if len(maxheap)>k:
          heapq.heappop(maxheap)
      
      res = []
      while len(maxheap)>0:
        dist, x, y = heapq.heappop(maxheap)
        res.append([x,y])
      return res
# Time Complexity: O(N log K)
  # We traverse N points, and each heap operation takes log K time. O(NlogK)
  # while maxHeap : O(KlogK).. travsere size k heap, and each time we perform heap opeartion O(logK)
# Space complexut : O(K)
  # Create siez K heap


def test():
  sol = Solution()
  points = [[0,2],[2,0],[2,2]]
  result = sol.kClosest(points,2)
  print(f"result: {result}")

if __name__ == "__main__":
    test()
















