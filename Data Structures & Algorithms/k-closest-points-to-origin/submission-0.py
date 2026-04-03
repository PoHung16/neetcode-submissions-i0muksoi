import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # keyword: "Top K elements with O(N) complexity”, “Two heaviest stones” -> Max/Min Heap
        # Image: A funnel holding only K spots; the farthest points (Max) get popped out.
        # 3-Step flow
        # Min heap (python default - heapq) : smallest value in the heap is at the root node 
        # Max heap : largest value in the heap is at the root node , in python, we use negative number to simulate this
        # Step 1:  Initialize Max-Heap/Min-Heap and build top k heap
        maxHeap = []  # Size will be at most K
        for x,y in points: #[0,2]
            dist = -(x ** 2 + y ** 2)
            heapq.heappush(maxHeap, [dist, x, y]) #[2,0,2] # will take first element of the list to heapify
            if len(maxHeap) > k: # If we have K+1 points, kick out the one that's farthest (the "Max")
                heapq.heappop(maxHeap)
        res = []
        # Step 2:  Traverse the heap to perform heap operation
        while maxHeap:
            dist, x, y = heapq.heappop(maxHeap)
            res.append([x,y])
        # Step 3:  return the result
        return res

# Time Complexity: O(N log K)
  # We process N points, and each heap operation takes log K time.
  # Heap push() & pop() : O(logN).... the element might have to "bubble"up  through the tree's height
  # Heap heapify() : O(N) because most nodes are near the bottom and don't have far to travel.When you do the math, it all balances out to linear time.
# Space complexut : O(K)
  # Create siez K heap




