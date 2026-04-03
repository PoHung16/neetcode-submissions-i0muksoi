import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
         # keyword: "Top K elements with O(N) complexity”, “Two heaviest stones” -> Max/Min Heap
        # Image: A funnel holding only K spots; the farthest points (Max) get popped out.
        # 3-Step flow
        # Min heap (python default - heapq) : smallest value in the heap is at the root node 
        # Max heap : largest value in the heap is at the root node , in python, we use negative number to simulate this
        # Step 1:  Initialize Max-Heap/Min-Heap and build top k heap
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap,num)
            if len(min_heap) > k: # If we have K+1 points, kick out the one that's farthest (the "Min")
                heapq.heappop(min_heap)
        # Step 2:  Traverse the heap to perform heap operation
        # Step 3:  return the result
        return min_heap[0]







        