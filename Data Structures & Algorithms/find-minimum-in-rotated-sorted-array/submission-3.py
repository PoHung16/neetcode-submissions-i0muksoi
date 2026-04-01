class Solution:
    def findMin(self, nums: List[int]) -> int:
        #思路：題目提到「Find/ Search in Sorted array」或「Logarithmic time - O(logn)」
        #題型：一般Binary Search 題型
        # Step 1: 初始化左右指針 和 res
        l = 0
        r = len(nums) -1
        res = nums[0]
        
        # Step 2: 循環 while L <= R「手沒交叉就不停」
        while l <= r:
            # Step 2-1: Trick - 如果沒有旋轉，直接找到最小值 
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            # Step 2-2: 更新res 並移動 mid指針
            
            mid = (l+r) //2
            res = min(res, nums[mid])
            #Step 2-3: 判斷哪半部是sorted array,最小值一定在另一邊 if nums[l] <= nums[mid]移動左右指針
            if nums[l] <= nums[mid]:
                l = mid +1
            else:
                r = mid -1
        #Step 3:回傳結果
        return res



