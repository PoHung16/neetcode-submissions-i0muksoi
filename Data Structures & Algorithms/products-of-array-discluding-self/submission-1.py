class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Step1:  初始化結果陣列，預設都放 1
        n = len(nums)
        res = [1] * n
        #Step2:  計算product of array
        #Step 2-1: 由左往右 (算左側積 Prefix) 
        prefix = 1
        for i in range(n):
            res[i] = prefix 
            prefix *= nums[i]
        #Step 2-2: 查由右往左 (算右側積 Suffix)
        postfix = 1
        for i in range(n-1,-1,-1):
            res[i] *= postfix 
            postfix *= nums[i]
        #Step 3: 回傳結果 
        return res




