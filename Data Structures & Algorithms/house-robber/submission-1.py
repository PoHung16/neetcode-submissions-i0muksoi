class Solution:
    def rob(self, nums: List[int]) -> int:
        #題型Keyword: 題型Keyword: “max/min profit, cost, ways, jumps” ->  Bottom up DP Tabulation / DP Constant
        #腦中圖像:  dp[i] 記住推導過的答案，用小問題的結果拼湊出大問題的解
        #動作記憶法 - 三個步驟
        #Step 1: Base Case + Initialize DP Tabulation Array 
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums[0],nums[1])
        # if you only need 2 steps, I can use prev, cur optimize to const sapce
        n = len(nums)
        prev = nums[0]
        curr = max(nums[0],nums[1])

        #Step 2: Traverse DP array with state transition formula
        for i in range(2,n):
            prev, curr = curr, max(curr, prev+nums[i])
    
        ##Step 3 return result
        return curr


# Time Complexity: O(n)....traverse n array
# Space Complexity: O(1).... constant space











        #dp[i] the maixmum amount of moeny you can get at this index