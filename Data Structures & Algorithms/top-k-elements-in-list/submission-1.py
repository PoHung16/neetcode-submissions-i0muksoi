class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #思路：找最大的 K 個元素 +分類/計數
        #題型：MinHeap題型 + 字母/數字計數器題型
        #Step 1:  Initiatize a map
        count = {}
        #Step 2:  Iterate over array 計數
        for num in nums:
            #Step2-2: Add the element to the Map 
            count[num] = count.get(num,0)+1
        #Step 1:  初始化一個空的 Min-Heap
        min_heap = []
        #Step 2: Iterate over hashmap to build heap
        for key in count.keys():
            #Step2-1: 將元素推入 Heap: heapq.heappush(heap, 
            heapq.heappush(min_heap, (count[key], key)) #頻率大小,  數字大小
            #Step2-2: 當heap長度 > k, ,pop out 最小的元素
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        #Step 3: 回傳結果
        res = []
        for i in range(k):
            res.append(heapq.heappop(min_heap)[1])
        return res




