class Solution:
    def climbStairs(self, n: int) -> int:
        # 題型Keyword:  “max/min profit, cost, ways, jumps” or fibonacci sequence ->  Bottom up DP Tabulation / DP Constant
        # 腦中圖像:  we only need the previous answer to find the current answer , we use dynamic programming to store the answer for the sub problem 
        # 動作記憶法 - 三個步驟 
        # ps.Edge case
        if not n:
            return 0
        # Step1: Base Case + Initialize DP Tabulation Array  or Initialize DP variable (if dp[i] only need less than 2 steps to get inferred)
        if n==1:
            return 1
        if n==2:
            return 2
        prev = 1
        curr = 2
        # Step 2: Traverse DP array with state transition formula
        for i in range(2,n):
            prev, curr = curr, prev + curr
        #Step 3 return result
        return curr
    
# Time Complexity: O(n)....traverse n array
# Space Complexity: O(1).... constant space

def test():
    sol = Solution()
    result = sol.climbStairs(2)
    print(f"Result : {result}")
test()









