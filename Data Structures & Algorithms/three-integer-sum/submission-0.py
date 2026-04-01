class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # 雙指針前提：必須先排序
        res = []
        
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]: continue # 跳過重複set
            
            # 下面這段就是 Two Sum II 模板,想成先固定一格數字，在計算後面的Two Sum
            # Step1:  初始化左、右指針
            l, r = i + 1, len(nums) - 1
            while l < r:
                #Step 2-1: 檢查目前的狀態
                three_sum = a + nums[l] + nums[r]
                #Step 2-2: 決定移動哪一個指針 
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1 # 找到後繼續找，並跳過重複set
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res

  