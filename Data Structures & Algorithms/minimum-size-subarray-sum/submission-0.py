# Optimal Solution
    # Goal:  O(N^2) -> O(N)
    # Keyword:  "Continuous Array/SubArray + Positive Numbers" -> Sliding Window (Variable Size) - edge case
    # Approach:  
        #1. Use two pointers (left and right) and a state variable to record window Sum
        #2. Expand from the right, and once condition happen ( state variable sum > target)
        #3. update the state variable & window size, then  shrink the window from the left
    
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # edge case
        if not nums:
            return 0
        min_length = float('inf')
        left = 0
        currentWindowSum = 0
        for right in range(len(nums)):
            currentWindowSum += nums[right]
            while currentWindowSum >= target:
                min_length = min(min_length,right-left+1)
                currentWindowSum -= nums[left]
                left += 1
        return min_length if min_length != float('inf') else 0
                
# Time complexity: O(N) ...traverse size N array
# Space complexity:  O(1)...create constant variable

def test():
    sol = Solution()
    target = 10
    nums = [2,1,5,1,5,3]
    result = sol.minSubArrayLen(target,nums)
    print(f"result:{result}")

if __name__ == "__main__":
    test()



        
        