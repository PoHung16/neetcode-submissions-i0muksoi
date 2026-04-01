class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #思路：題目提到「連續子陣列」或「連續子字串」 - 陣列中有負數
        #題型：Prefix Sum題型
        #腦內圖像：冒險者 (Current Sum): 一邊走路，一邊把路上的數字加進包包裡， 
        #配合一個currentSum歷史紀錄本 
        #計算currentSum - prefixSum = k的個數
        #計算prefixSum = currentSum - k的個數

        #Step1:  準備冒險者工具
        count = 0
        currentSum = 0
        history = {0:1}
        #Step2:  For-loop遍遞陣列
        for num in nums:
            #Step 2-1: 冒險者前進，把路上的數字加進包包裡
            currentSum += num
            prefixSum = currentSum - k
            #Step 2-2: 查帳本，過去有沒有出現過 (cur_sum - k)的prefixSum, 加入計數
            if prefixSum in history:
                count += history[prefixSum]
            history[currentSum] = history.get(currentSum,0) + 1
            #Step 2-3: 把current_Sum加入歷史帳本
        #Step 3: 回傳結果 
        return count










