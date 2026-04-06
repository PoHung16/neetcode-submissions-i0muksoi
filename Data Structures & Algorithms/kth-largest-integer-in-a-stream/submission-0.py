import heapq
    # A. Clarify the goal: keep track of the $kth largest element
    # B. Decide the data strucure
        # sort(too slow) : O(M* NlogN) -> M is the is the number of calls made to add()
        # min heap
    # C. Implement constructor and method

    # Keyword : Top K elements  -> Min Heap
    # Image :  Imagine a smart funnel that only holds K spots, and the weakest/biggest ones get kicked out the top, where new elements "bubble" into place
    # 3-Step Flow
    # Step 1:  Initialize Max-Heap/Min-Heap simulation
    # Step 2:  Traverse the heap to perform heap operation
    # Step 3:  return the result
class KthLargest:    
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = nums
        heapq.heapify(self.min_heap)
        while len(self.min_heap)>k:
            heapq.heappop(self.min_heap)
    def add(self, val:int) -> int:
        heapq.heappush(self.min_heap,val)
        if len(self.min_heap)>self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]

# Time Complexity: 
#   Init: O(N log K) 
    # heapify: O(N)
    # Traverse the heap to perform heap operation: (N-K)次 每次heappop: O(logK)
    # Time = O(N) + O(N-K)logK = O(NlogK)
#   Add: O(log K) 
# Space Complexity: O(K) - we create size K heap

   
    