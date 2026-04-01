class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Step1:  初始化左、右指針
        l, r = 0, len(height) - 1
        res = 0

        #Step2:  while left< right
        while l < r:
            # Step 2-1: 檢查目前的狀態: 計算目前面積
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)
            
            #Step 2-2: 決定移動哪一個指針:捨棄短板 (關鍵！)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res