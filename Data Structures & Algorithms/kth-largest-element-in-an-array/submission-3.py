import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
      # Keyword : Top K elements  -> Min Heap
      # Image :  Imagine a smart funnel that only holds K spots, and the weakest/biggest ones get kicked out the top, where new elements "bubble" into place
      # 3-Step Flow
      # Step 1:  Initialize Max-Heap/Min-Heap simulation
      # Step 2:  Traverse the array to perform heap operation
      # Step 3:  return the result
      min_heap = []
      for num in nums:
        heapq.heappush(min_heap,num)
        if len(min_heap) > k :
          heapq.heappop(min_heap)
      return min_heap[0]
      
# Time Complexity: O(N log K)
  # We process N points, and each heap operation takes log K time.
  # Heap push() & pop() : O(logN).... the element might have to "bubble"up  through the tree's height
# Space complexut : O(K)
  # Create siez K heap
def test():
  sol = Solution()
  nums = [2,3,1,5,4]
  result = sol.findKthLargest(nums,2)
  print(f"result: {result}")

test()





        