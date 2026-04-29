"""
 OOD: Yes
 Constraints: No
 input : constructor/method
 output : constructor/method
"""
# A. Clarify the goal: find the $kth largest element in the stream
# B. Decide the data strucure
    # Keyword: Top K elements -> Max/Min Heap
    # Image :build a heap that only holds K spots traverse the array, and the weakest/biggest ones get kicked out the top, where new elements "bubble" into place
 # C. Implement constructor and method

from typing import List
import heapq
class KthLargest:
    def __init__(self,k:int,nums: List[int]):
        self.min_heap = nums
        self.k = k
        heapq.heapify(self.min_heap)
        while len(self.min_heap)>k:
            heapq.heappop(self.min_heap)
                
    def add(self, val:int)-> int:
        heapq.heappush(self.min_heap,val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]

def test():
    kthLargest = KthLargest(3, [1, 2, 3, 3])
    result1 = kthLargest.add(3);   
    result2 = kthLargest.add(5);   
    result3 = kthLargest.add(6);   
    result4 = kthLargest.add(7);   
    result5 = kthLargest.add(8);   

    print(f"Result:{result1}")
    print(f"Result:{result2}")
    print(f"Result:{result3}")
    print(f"Result:{result4}")
    print(f"Result:{result5}")
    
if __name__ == "__main__":
    test()

# Time Complexity: 
# Constructor: O(NlogK)
    # heapify: O(N)
    # Traverse the heap to perform heap operation: (N-K)次 每次heappop: O(logK)
    # Time = O(N) + O(N-K)logK = O(NlogK)
# Add: O(log K) ...push the elment into size K heap
# Space Complexity: O(K) - we create size K heap




    