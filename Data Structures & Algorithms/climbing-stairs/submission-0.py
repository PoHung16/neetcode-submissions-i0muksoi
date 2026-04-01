class Solution:
    def climbStairs(self, n: int) -> int:
        #題型Keyword: 題型Keyword: “max/min profit, cost, ways, jumps” ->  Bottom up DP Tabulation / DP Constant
        #腦中圖像:  dp[i] 記住推導過的答案，用小問題的結果拼湊出大問題的解
        #動作記憶法 - 三個步驟 
        #Step 1:   Base Case + Initialize DP Tabulation Array 
        if n==1: return 1
        if n==2: return 2
        # if you only need 2 steps, I can use prev, cur optimize to const sapce
        prev = 1
        curr = 2
        #Step 2:  Traverse DP array with state transition formula
        # start from the 3 one
        for i in range(2,n):
            prev, curr = curr , prev + curr
        #Step 3 : Return result :Return Dp final element
        return curr
# Time Complexity: O(n)....traverse n array
# Space Complexity: O(1).... constant space