"""
 OOD: No
 Constraints: No
 input : List[int]
 output : int
"""
# Keyword:  Two heaviest stones -> Heap Process Simulation
# Image :build a heap traverse the array, Always smash the biggest two, and let the Heap do the work
# Tricks:
    # If You need to keep all element in a heap bc we are not sure if y-x will be the heavies stone later on , instead of Top K in the heap, you need to use heapify to build the whole heap
import heapq
from typing import List
class Solution:
    def lastStoneWeight(self, stones:List[int])-> int:
        maxheap = [-s for s in stones]
        heapq.heapify(maxheap)
        while len(maxheap)>1:
            y = heapq.heappop(maxheap)
            x = heapq.heappop(maxheap)
            if x != y:
                heapq.heappush(maxheap,y-x)
        return -maxheap[0] if maxheap else 0

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
# Space Complexity: O(n)...we build size N heap

