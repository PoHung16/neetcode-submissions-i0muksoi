import heapq

class MedianFinder:
    # Keyword: Find Median From Data Stream -> Dual heap
    # Image: 想像你有一個天秤。左邊是一個 Max-Heap (大頂堆)，存比較小的那半部數字；右邊是一個 Min-Heap (小頂堆)，存比較大的那半部數字。 #中位數在哪？ 就在這兩個堆的「頂端」！
    # 3-Step Flow
    #Step 1:  Initialize Max-Heap/Min-Heap 
    #Step 2:  Traverse the array to perform heap operation
    #Step 3:  return the result
    def __init__(self):
        # A. Clarify the goal: keep track of the median in a stream
        # B. Decide the data structure: Dual Heaps (Balance the scale)
        self.small = [] # Max-Heap (stores negative numbers)
        self.large = [] # Min-Heap
    
    def addNum(self, num: int) -> None:
        # Traverse & Rebalance
        # 1. 永遠先推入 small (Max-Heap)
        heapq.heappush(self.small, -num)
        
        # 2. 為了維持順序，把 small 最大的彈給 large (Min-Heap)
        heapq.heappush(self.large, -heapq.heappop(self.small))
        
        # 3.如果 large 變得比 small 多，就把 large 的最小值彈回來給 small,確保 small 的最大值 <= large 的最小值。
        #如果不彈回來： 奇數時，中位數可能在左邊，也可能在右邊。你每次都要寫 if 去判斷誰比較多。
        #如果彈回來： 只要 len(small) > len(large)，中位數就一定是 small[0]。
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        #odd
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        #even
        return (-self.small[0] + self.large[0]) / 2.0

# Time: 
  #addNum(num): O(logN) ... we perform 3 heap operation
  #findMedian():O(1)
# Space:
  #為了計算中位數，我們必須儲存流中出現過的所有數字, the total size of small/ large heap is N







