import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Keyword : Top K elements  -> Min Heap
        # Image :  Imagine a smart funnel that only holds K spots, and the weakest/biggest ones get kicked out the top, where new elements "bubble" into place
        # 3-Step Flow
        # Step 1:  Initialize Max-Heap/Min-Heap simulation
        # Step 2:  Traverse the array to perform heap operation
        # Step 3:  return the result
        maxHeap = []
        for x,y in points:
          dist = -(x**2 + y**2)
          heapq.heappush(maxHeap,(dist,x,y))
          if len(maxHeap) > k:
            heapq.heappop(maxHeap)
        res = []
        while maxHeap:
          dist, x, y = heapq.heappop(maxHeap)
          res.append([x,y])
        return res

# Time Complexity: O(N log K)
  # We process N points, and each heap operation takes log K time.
  # Heap push() & pop() : O(logN).... the element might have to "bubble"up  through the tree's height
  # Heap heapify() : O(N) because most nodes are near the bottom and don't have far to travel.When you do the math, it all balances out to linear time.
# Space complexut : O(K)
  # Create siez K heap
def test():
  sol = Solution()
  points = [[0,2],[2,0],[2,2]]
  result = sol.kClosest(points,2)
  print(f"result: {result}")

test()



