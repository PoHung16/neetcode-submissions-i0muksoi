class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Step1:  初始化左、右指針
        l, r = 0, len(numbers) - 1
        # Step2:  while left< right
        while l < r:
            #Step 2-1: 檢查目前的狀態
            curSum = numbers[l] + numbers[r]
            #Step 2-2: 決定移動哪一個指針 (這是最關鍵的一步！)
            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []