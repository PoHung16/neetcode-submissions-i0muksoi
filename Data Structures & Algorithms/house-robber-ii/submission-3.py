class Solution:
    def rob(self, nums: List[int]) -> int:
        # 題型Keyword:  “max/min profit, cost, ways, jumps” or fibonacci sequence ->  Bottom up DP Tabulation / DP Constant
        # 腦中圖像:  we only need the previous answer to find the current answer , we use dynamic programming to store the answer for the sub problem 
        # 動作記憶法 - 三個步驟
        # compare house_robber_linear 
        # 第1種情況：搶第 2 間到最後一間 (1 到 n-1)
        # 第2種情況：搶第 1 間到倒數第 2 間 (0 到 n-2)
        if not nums:
            return 0 
        n = len(nums)
        if n==1:
            return nums[0]
        n = len(nums)
        return max(self.rob_linear(nums[1:]),self.rob_linear(nums[0:-1]))

    def rob_linear(self,nums: List[int]) -> int:
        if not nums:
            return 0 
        n = len(nums)
        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0],nums[1])
        prev = nums[0]
        curr = max(nums[0],nums[1])

        for i in range(2,n):
            prev, curr = curr, max(curr,prev+nums[i])
        return curr

# Time Complexity: O(n)....traverse n array
# Space Complexity: O(1).... constant space
def test():
    sol = Solution()
    result = sol.rob([3,4,3])
    print(f"Result : {result}")
test()

       


        