"""
 OOD: No
 Constraints: No
 input : List[int] , integer
 output : List[int]
"""
# Brute Force: 
    # Use hashMap to count frequency, and sort the hashmap's value, and get the top k ->O(N+NlogN)
class Solution:
    def topKFrequent(self, nums:List[int], k:int)-> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            hashMap[nums[i]] = hashMap.get(nums[i],0)+1
        sorted_items = sorted(hashMap.keys(), key=lambda x:hashMap[x], reverse=True)
        return sorted_items[0:k]

# Optimal Soltion:
    # Keyword : “Top K elements” -> Max/Min Heap
    # Approach:  Use hashMap to count frequency, Use Heap holds K spots to traverse array , and the weakest/largest one get kicked out of heap, new element bubble in
    # Tricks
        # 1. If you want to traverse a map, map.items() or map.keys() or map.values()
        # 2. You can push multiple value into heap, heap will take first argument to make comparsion
"""
1.Heaps are complete binary trees, which means that all levels of the tree are fully filled except for the last level, which is filled from left to right.
2.Min heap (python default - heapq) : smallest value in the heap is at the root node 
3.Max heap : largest value in the heap is at the root node , in python, we use negative number to simulate this
"""
from typing import List
import heapq
class Solution:
    def topKFrequent(self, nums:List[int], k:int)-> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            hashMap[nums[i]] = hashMap.get(nums[i],0)+1
        min_heap = []
        for number,count in hashMap.items():
            heapq.heappush(min_heap,(count,number))
            if len(min_heap)>k:
                heapq.heappop(min_heap)
        res = []
        for count, number in min_heap:
            res.append(number)
        return res
            
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

def test():
    sol = Solution()
    nums = [1,2,2,3,3,3]
    k = 2
    result = sol.topKFrequent(nums,k)
    print(f"Result: {result}")

if __name__  == "__main__":
    test()








