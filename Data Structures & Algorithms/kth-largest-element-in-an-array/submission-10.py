"""
 OOD: No
 Constraints: No
 input : List[int], int
 output : int
"""
# Brute Force: 
    # sort the entire array, and return the top points.-> O(NlogN) 
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
      nums.sort(reverse=True)
      return nums[k-1]

# Optimal Solution
  # Goal: O(NlogN)-> O(logN).. don't sort the whole array every time
  # Keyword: Top K elements -> Min Heap
  # Approach : Traverse an array and  build a heap that only holds K spots, then kick out the smallest one on the top,  where new elements "bubble" into place

from typing import List
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
      min_heap = []
      for num in nums:
        heapq.heappush(min_heap,num)
        if len(min_heap)>k:
          heapq.heappop(min_heap)
      return min_heap[0]
      
# Time Complexity: O(N log K)
  # Traverse the array to perform heap operation: N次 每次heappop: O(logK)
# Space complexut : O(K)
  # Create siez K heap
def test():
  sol = Solution()
  nums = [2,3,1,5,4]
  result = sol.findKthLargest(nums,2)
  print(f"result: {result}")
if __name__ == "__main__":
    test()    
    








        