class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 題型Keyword: "Sum without + or -"
        # 腦中圖像: 「加法器」 — AND 往左移一格是「進位」，XOR 是「不進位加法」
        # Step 1: Python 的整數是無限長的，所以要用 32-bit mask 模擬溢位(8 bytes)
        mask = 0xFFFFFFFF
        
        # Step 2: Iterate the loop to process b & mask - 位元剪刀, 只留下右邊那 32 位元
        while (b & mask) > 0: 
            # 1. 先算出「進位」(Carry)並往左移一格
            carry = (a & b) << 1
            # 2. 再算出「不進位加法」(Sum without carry)
            a = a ^ b
            # 3. 把carry存入b 繼續和a相加
            b = carry
            
        #Step 3 : Return result
        #兩個很大的正數相加造成overflow,因為有 mask，b & mask 會變成 0 導致迴圈停止。
        #但b>0，要把超過的負數cut off(位元剪刀)    
        return (a & mask) if b > 0 else a

        '''
        Time Complexity : O(1) -> 雖然是 while，但 32-bit 系統最多跑 32 次
        Space Complexity : O(1) -> 只用了 carry 一個變數
        '''


