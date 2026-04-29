"""
 OOD: No
 Constraints: No
 input : List[int], int
 output : int
"""
# Keyword: Top K elements -> Max/Min Heap
# Image :build a heap that only holds K spots traverse the array, and the weakest/biggest ones get kicked out the top, where new elements "bubble" into place

from typing import List
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
      minHeap = []
      for num in nums:
        heapq.heappush(minHeap,num)
        if len(minHeap)>k:
          heapq.heappop(minHeap)
      return minHeap[0]
def test():
  sol = Solution()
  nums = [2,3,1,5,4]
  result = sol.findKthLargest(nums,2)
  print(f"result: {result}")
if __name__ == "__main__":
    test()    
    

# Time Complexity: O(N log K)
  # Traverse the array to perform heap operation: N次 每次heappop: O(logK)
# Space complexut : O(K)
  # Create siez K heap







        