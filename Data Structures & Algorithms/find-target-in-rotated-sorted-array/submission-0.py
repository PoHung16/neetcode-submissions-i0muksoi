class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #search: 6
        # Step 1:初始化
        l = 0
        r = len(nums) -1
        # Step 2 :循環
        while l <= r:
            mid = (l + r) //2
            if nums[mid] == target:
                return mid
            # Step 3 :左半部順 234|561
            if nums[l] <= nums[mid]:
                # Step 4 :判斷範圍
                if nums[l] <= target < nums[mid] :
                    # Step 5: 移動
                    r = mid -1
                else:
                    l = mid + 1
            #左半部如果不順，右邊那半部一定是「順」的 561 | 234
            else:
                if nums[mid] < target <= nums[r] :
                    l = mid +1
                else:
                    r = mid -1
        return -1



            


        


        