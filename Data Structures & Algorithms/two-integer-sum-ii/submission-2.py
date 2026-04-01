class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 題型Keyword: Sorted Array ->  Two Pointers Basic
        # 腦中圖像: Opposite pointer左右靠近 
        # 動作記憶法 - 3個步驟 
        # Step1:   Initialize l,r pointer
        l, r = 0, len(numbers) - 1
        # Step2:  Traverse String: while left< right
        while l < r:
            #Step 2-1: 檢查目前的狀態
            curSum = numbers[l] + numbers[r]
            #Step 2-2: 決定移動哪一個指針 
            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []
# Time complexity: O(N) ...traverse size N array
# Space complexity:  O(1)....create constant variable
def test():
    sol = Solution()
    result = sol.twoSum([1,2,3,4],3)
    print(f"Result: {result})")
test()


