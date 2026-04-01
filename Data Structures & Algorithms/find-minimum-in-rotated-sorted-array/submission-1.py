class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Step 1:初始化
        res = nums[0]
        l = 0
        r = len(nums) -1 
        # Step 2 :循環
        while l <= r:
            # Step 2.5: 捷徑Trick:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            mid = (l+r) //2
            res = min(res, nums[mid])
            # Step 3 :找左半部順or右半部順
            if nums[l] <= nums[mid]:
                # Step 4 :判斷範圍 + Step 5移動
                l = mid +1
            else:
                r = mid -1
        #Step 6:回傳結果
        return res

