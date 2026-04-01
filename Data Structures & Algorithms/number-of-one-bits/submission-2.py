class Solution:
    def hammingWeight(self, n: int) -> int:
        # 題型Keyword: “Bits”,  “Binary Representation”
        # 腦中圖像: “輸送帶 (The Conveyor Belt)” — 數字像一排零件在帶子上。
        # 動作記憶法 - 三個步驟
        #Step 1: Initialize 新輸送帶 or counter or counter array
        count = 0
        #Step 2: Iterate the loop to process 32 bits 舊輸送帶
        for _ in range(32):
            # 1. 舊輸送帶抓出目前的零件 (n 的最後一位)
            bit = n & 1
            # 2. 舊輸送帶移位(換下一個零件過來)
            n = n >> 1
            # 3. counter計數
            count += 1 if bit else 0
           
        #Step 3 : Return result
        return count
        '''
        Time: O(1)
            O(32)... traverse 32 bits
        Space: O(1) ...create single variable
        '''
