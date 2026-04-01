class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Step 1: 把所有數字丟進 Set 裡
        # Set 的查詢是 O(1)，這是達成 O(n) 的關鍵
        numSet = set(nums)
        longest = 0
        
        # Step 2: 遍歷每一個數字
        for n in nums:
            # Step 2-1: 檢查這是不是一個序列的「起點」
            # 如果 n - 1 在 Set 裡，代表 n 只是某個序列的中間，我們跳過它
            if (n - 1) not in numSet:
                length = 1
                # Step 2-2: 從起點開始往後數
                while (n + length) in numSet:
                    length += 1
                
                # Step 2-3: 更新最大長度
                longest = max(length, longest)
                
        return longest