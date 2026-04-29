"""
 OOD: No
 Constraints: No
 input : List[int]
 output : int
"""
# Keyword:  Two heaviest stones” -> Heap Process Simulation
# Image :build a heap that only holds K spots traverse the array, Always smash the biggest two, and let the Heap do the work
import heapq
from typing import List
class Solution:
    def lastStoneWeight(self, stones:List[int])-> int:
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            y = heapq.heappop(max_heap) # Heaviest
            x = heapq.heappop(max_heap) # Second heaviest
            if x != y:
                heapq.heappush(max_heap, y - x) # Push the difference back
        return -max_heap[0] if max_heap else 0
def test():
    sol = Solution()
    stones = [2,3,6,2,4]
    result = sol.lastStoneWeight(stones)
    print(f"Result:{result}")
if __name__ == "__main__":
    test()

# Time complexity: O(NlogN)
  # Building the heap, heapify:  O(N)
  # Heap push() & pop(): In the worst case, we perform n−1 times smashes. O(NlogN)
# Space Complexity: O(n)...we build size K heap

