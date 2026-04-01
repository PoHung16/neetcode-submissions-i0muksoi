class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #思路： 資料已經排序 - 找對應的「一對」或「一組」數字 
        #題型：  Opposite pointer 題型
        #腦內圖像：固定一個數字先，再去用Two pointer 解Two Sum。有2個地方要避免重複的
        res = []
        nums.sort()
        for i, value in enumerate(nums):
            # 跳過重複set
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # 下面這段就是 Two Sum II 模板,想成先固定一格數字，在計算後面的Two Sum
            # Step1:  初始化左、右指針
            l = i+1
            r = len(nums)-1
            while l < r:
                #Step 2-1: 檢查目前的狀態
                threeSum = value + nums[l] + nums[r]
                #Step 2-2: 決定移動哪一個指針 
                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    res.append([value, nums[l], nums[r]])
                    l += 1
                    # 跳過重複set
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
        return res



        