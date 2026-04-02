import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # keyword: "Top K elements with O(N) complexity”, “Two heaviest stones” -> Max/Min Heap
        # Image: Imagine a smart funnel that only holds K spots, and the weakest/biggest ones get kicked out the top, where new elements "bubble" into place
            # Max Heap: The largest stone is always at the root. in python, we use negative number to simulate this
        # 3-Step flow
        # Step 1: Initialize Max-Heap simulation
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)

        # Step 2: Traverse the array to build up heap
        while len(max_heap) > 1:
            y = heapq.heappop(max_heap) # Heaviest
            x = heapq.heappop(max_heap) # Second heaviest

            if x != y:
                heapq.heappush(max_heap,y-x) # Push the difference back
        
        # Step 3:
        return -max_heap[0] if max_heap else 0
# Time complexity:
  # Heap push() & pop() : O(logN).... the element might have to "bubble"up  through the tree's height
  # Heap heapify() : O(N) because most nodes are near the bottom and don't have far to travel.When you do the math, it all balances out to linear time.
# Space complexut : O(N).. .we create size N heap

def test():
    sol = Solution()
    stones = [2,3,6,2,4]
    result = sol.lastStoneWeight(stones)
    print(f"Result:{result}")
test()