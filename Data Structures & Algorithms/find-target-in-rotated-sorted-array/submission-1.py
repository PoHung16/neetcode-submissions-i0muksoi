class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Step 1:初始化
        l = 0
        r = len(nums) - 1
        # Step 2 :循環
        while l <=r :
            mid = (l + r)//2
            if nums[mid] == target:
                return mid
            # Step 3 :左半部順 
            if nums[l] <= nums[mid]:
                # Step 4 :判斷範圍
                if nums[l] <= target < nums[mid]:
                    # Step 5: 移動
                    r = mid - 1
                else:
                    l = mid + 1
            # Step 3 :右半部順 
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            # Step 6:回傳結果
        return -1











        