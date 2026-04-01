class Solution:
    def countBits(self, n: int) -> List[int]:
        # 題型Keyword: “Bits”,  “Binary Representation”
        # 腦中圖像: “輸送帶 (The Conveyor Belt)” — 數字像一排零件在帶子上。
        # 動作記憶法 - 三個步驟

        #Step 1: Initialize 新輸送帶 or counter or counter array
        count = [0]
        #Step 2: Iterate the loop to process bits 舊輸送帶
        for i in range(1,n+1): # 0 index is already created
            count.append(count[i//2]+i%2)

        #Step 3 : Return result
        return count

        # even :every even number double, it will still have the same amout of number as it divide by 2, based on the pattern
        # odd: add 1 from the previous even number

        '''
        Time: O(N)...traverse N Bits
        Space: O(N) ...create N lists
        '''
