"""
 OOD: No
 Constraints: No
 input : List[int] , integer
 output : List[int]
"""
"""
1.Heaps are complete binary trees, which means that all levels of the tree are fully filled except for the last level, which is filled from left to right.
2.Min heap (python default - heapq) : smallest value in the heap is at the root node 
3.Max heap : largest value in the heap is at the root node , in python, we use negative number to simulate this
"""
# Keyword : 
    # 1. “Two Sum", "Duplicate", "Frequency count", "Matching pairs", "Anagrams" -> Basic HashMap
    # 2. “Top K elements” -> Max/Min Heap
# Image :   
    #1. Imagine an instant-lookup Map Traverse an array to check if a Key or Value exists before , then perform following actions 
    #2. Imagine a heap only holds K spots traverse the array, and the weakest/biggest ones get kicked out the top, where new elements "bubble" 
# Tricks: 
    # 1. If you want to traverse a map, map.items() or map.keys() or map.values()
    # 2. You can push multiple value into heap, heap will take first argument to make comparsion
        
from typing import List
import heapq
class Solution:
    def topKFrequent(self, nums:List[int], k:int) -> List[int]:
        # we should use hashmap to store which number has largest count
        hashMap = {}
        for i in range(len(nums)):
            hashMap[nums[i]] = hashMap.get(nums[i],0)+1
        min_heap = []
        # use min_heap to select top k largest count
        for number,count in hashMap.items():
            heapq.heappush(min_heap,(count,number))
            if len(min_heap)>k:
                heapq.heappop(min_heap)
        res = []
        for count, number in min_heap:
            res.append(number)
        return res
        
    
def test():
    sol = Solution()
    nums = [1,2,2,3,3,3]
    k = 2
    result = sol.topKFrequent(nums,k)
    print(f"Result: {result}")

if __name__ == "__main__":
    test()


# Time complexity:(NlogK)
    # Traverse size N Array to put into Map: O(N)
    # Traverse size N Map to peform heap operation: O(NlogK)
    # Traverse size k Heap: O(K)
    # O(NlogK)> O(N) > O(K)
#  Space complexity:   O(N)
    # O(N)....create size N HashMap     
    # O(K) - we create size K heap
    # O (K) -  we create size K res
    # O(N) > O(K)





