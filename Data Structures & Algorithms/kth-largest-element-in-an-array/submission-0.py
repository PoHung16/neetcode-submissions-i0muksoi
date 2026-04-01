class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #Ps.先想有沒有edge case,直接return False->有
        if not nums:
            return
        #Step 1:  初始化一個空的 Min-Heap
        min_heap = []

        #Step 2:  Iterate over array to build heap
        for num in nums:
            #Step2-1: 當heap長度<k , 將元素推入 Heap
            if len(min_heap) < k:
                heapq.heappush(min_heap,num)
            #Step2-2: 當heap長度 >= k, 先 推入新的元素 ,pop out 最小的元素
            else:
                heapq.heappushpop(min_heap,num)
        #Step2-3: 現在heap裡面是Top k個的元素,因為小的都被踢掉了， 只要return min_heap[0]就是topK 大的元素
        return min_heap[0]






        