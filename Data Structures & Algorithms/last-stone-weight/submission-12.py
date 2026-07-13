"""
 OOD: No
 Constraints: No
 input : List[int]
 output : int
"""
# Brute Force: 
    # Sort the array on every turn to pull out the two heaviest stones at the end, smash them, and append any remainder back -> O(N^2logN).. for every element, you need to sort all the array
from typing import List
class Solution:
    def lastStoneWeight(self,stones:List[int])-> int:
        while len(stones)>1:
            stones.sort()
            y = stones.pop()
            x = stones.pop()
            if x != y:
                stones.append(y-x)
        return stones[0] if stones else 0 

# Optimal Solution
    # Goal: O(N^2logN)-> O(NlogN).. don't sort the whole array every time
    # Keyword : “Two heaviest stones”, “Most Frequent Element Cooldown Period” -> Heap Simulation
    # Approach: Use Maxheap to extract 2 heaviest element and push remainder back
# Tricks:
    # Use Top-K (Size-Limited Heap): When you only care about the absolute K largest or smallest elements overall.
    # Use Full Heapify: When elements change dynamically (like y−x) and can become the new largest/smallest elements later.

import heapq
from typing import List
class Solution:
    def lastStoneWeight(self, stones:List[int])-> int:
        maxheap = [-s for s in stones]
        heapq.heapify(maxheap)
        while len(maxheap)>1:
            y = -heapq.heappop(maxheap)
            x = -heapq.heappop(maxheap)
            if x != y:
                heapq.heappush(maxheap,-(y-x))
        return -maxheap[0] if maxheap else 0 
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


