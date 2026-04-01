class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #思路：題目提到「Find/ Search in Sorted array」或「Logarithmic time - O(logn)」
        #題型：一般Binary Search 題型
        #腦內圖像：判斷哪邊是sorted array,因為本題旋轉過
        #Step 1: 初始化左右指針 
        l = 0
        r = len(nums) - 1
        # Step 2: 循環 while L <= R「手沒交叉就不停」
        while l <=r :
            #Step 2-1: 計算 mid 並更新結果
            mid = (l + r)//2
            #Step 2-2: nums[mid] == target直接回傳
            if nums[mid] == target:
                return mid
            # Step 2-3: 判斷哪半部是sorted array, 就在哪邊binary search, if nums[l] <= nums[mid],移動左右指針
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        # Step 3:回傳結果
        return -1
        '''
        Time : O(LogN) …Since its divided by h times, 2^h = n, h = logN
        Space: O(1) ..  We didn't create extra variable or data structure
        '''












        