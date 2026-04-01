class Solution:
    def rob(self, nums: List[int]) -> int:
        # 題型Keyword:  “max/min profit, cost, ways, jumps” or fibonacci sequence ->  Bottom up DP Tabulation / DP Constant
        # 腦中圖像:  we only need the previous answer to find the current answer , we use dynamic programming to store the answer for the sub problem 
        # 動作記憶法 - 三個步驟
        # ps.Edge case
        if not nums:
            return 0
        # Step1: Base Case + Initialize DP Tabulation Array  or Initialize DP variable (if dp[i] only need less than 2 steps to get inferred)
        n = len(nums)
        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0] ,nums[1])
        
        prev = nums[0]
        curr = max(nums[0] ,nums[1])

        # Step 2: Traverse DP array with state transition formula
        for i in range(2,n):
            prev,curr = curr, max(curr, prev+nums[i])

        #Step 3 return result
        return curr
# Time Complexity: O(n)....traverse n array
# Space Complexity: O(1).... constant space
def test():
    sol = Solution()
    result = sol.rob([1,1,3,3])
    print(f"Result : {result}")
test()









       