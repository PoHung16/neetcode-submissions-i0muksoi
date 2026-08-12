"""
 OOD: No
 Constraints: No
 input : List[int]
 output : int
"""
# Brute Force: 
    # Array - Sort the array on every turn to pull out the two heaviest stones at the end, smash them, and append any remainder back -> O(N* NlogN).. for every element, you need to sort all the array
from typing import List
class Solution:
    def lastStoneWeight(self,stones:List[int])->int:
        while len(stones)>1:
            stones.sort()
            y = stones.pop()
            x = stones.pop()
            if x != y:
                stones.append(y-x)
        return stones[-1]

# Optimal Solution
    # Goal: O(NlogN)-> O(N)
    # Keyword : “Two heaviest stones”-> Heap Simulation
    # Approach: Use Maxheap to extract 2 heaviest element and push remainder back
# Tricks:
    # Use Top-K heap (Size-Limited Heap): When you only care about the absolute K largest or smallest elements overall.
    # Use Full Heapify: Make sure every stone is being processed

from typing import List
import heapq
class Solution:
    def lastStoneWeight(self, stones:List[int])-> int:
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)
        while len(max_heap)>1:
            y = -heapq.heappop(max_heap)
            x = -heapq.heappop(max_heap)
            if x != y:
                heapq.heappush(max_heap,-(y-x))
        
        return -max_heap[0] if max_heap else 0

# Time complexity: O(NlogN)
  # Building the heap, heapify:  O(N)     
  # Heap push() & pop(): In the worst case, we perform n−1 times smashes. O(NlogN) 
# Space Complexity: O(n)...we build size N heap

def test():
    sol = Solution()
    stones = [2,3,6,2,4]
    result = sol.lastStoneWeight(stones)
    print(f"Result:{result}")
if __name__ == "__main__":
    test()










