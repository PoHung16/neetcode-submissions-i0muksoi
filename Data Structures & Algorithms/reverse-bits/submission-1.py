class Solution:
    def reverseBits(self, n: int) -> int:
        # 題型Keyword: 輸送帶掃描法 (The Conveyor Belt)
        # 腦中圖像: “輸送帶 (The Conveyor Belt)” — 數字像一排零件在帶子上。
        # 動作記憶法 - 三個步驟
        # Step 1: Initialize 新輸送帶 res
        res = 0
        #Step 2: Iterate the loop to process 輸送帶零件
        for _ in range(32):
            # 1. 舊輸送帶抓出目前的零件 (n 的最後一位)
            bit = n & 1
            # 2. 舊輸送帶移位(換下一個零件過來)
            n = n >> 1
            # 3. 新輸送帶騰出位子 (叫舊零件往左移一格)
            res = res << 1
            # 4. 塞進零件 (把零件放入 res 的空位)
            res = res | bit
            
       
            
        return res