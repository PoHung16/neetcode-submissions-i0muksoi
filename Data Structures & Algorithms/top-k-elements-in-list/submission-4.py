from typing import List
import heapq
class Solution:
    def topKFrequent(self, nums:List[int], k:int) -> List[int]:
        # Keyword : "Frequency count" -> HashMap
        # Image: Imagine an instant-lookup Map where you check if a Key or Value exists before , then perform following actions
        # Worlfow
        # Step 1:  Initialize a map, store the key-value pair
        # Step 2:  Traverse the Array to  check if a  a Key or Value exists before, then perform following actions
        # Step 3: Return the result
        # Tricks: If you want to traverse a map, map.items() or map.keys() or map.values()
        count = {}
        for num in nums:
            count[num] = count.get(num,0)+1
        # Keyword : Top K elements -> Min Heap/Max Heap 
        # Image : Imagine a smart funnel that only holds K spots, and the weakest/biggest ones get kicked out off the top, where new elements "bubble" into place
        # Worlfow
        # Step 1 : initialize  Max-Heap/Min-Heap 
        # Step 2:  Traverse the array to perform heap operation
        # Step 3: Return the result
        # Tricks :
            # You can push multiple value into heap, heap will take first argument to  make comparsion
        min_heap = []
        for key,value in count.items():
            heapq.heappush(min_heap,[value,key])
            if len(min_heap)>k:
                heapq.heappop(min_heap)
        return [element[1] for element in min_heap]
        

# Time complexity:(NlogK)
    # Traverse size N Array: O(N)
    # Traverse size N Map to build the map: O(NlogK)
    # O(NlogK)> O(N)
#  Space complexity:   O(N)
    # O(N)....create size N HashMap     
    # O(K) - we create size K heap
    # O(N) > O(K)

def test():
    sol = Solution()
    nums = [1,2,2,3,3,3]
    k = 2
    result = sol.topKFrequent(nums,k)
    print(f"Result: {result}")
test()
    


