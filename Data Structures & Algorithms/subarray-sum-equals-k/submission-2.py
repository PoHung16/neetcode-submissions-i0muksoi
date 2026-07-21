"""
 OOD: No
 Constraints: No
 input : List[int], int
 output : int
"""
# Brute Force: 
    # Array - Use nested loop to calculate if subarray sums match target from different start to different end -> O(N^2)
class Solution:
    def subarraySum(self, nums:List[int],target:int) -> int:
        count = 0
        for i in range(len(nums)):
            currentSum = 0
            for j in range(i,len(nums)):
                currentSum += nums[j]
                if currentSum == target:
                    count+=1
        return count

# Optimal Soltion:
    # Goal: O(N^2) / O(NlogN) -> O(N)
    # Keyword : "Contiguous Subarray + Negative Numbers" -> HashMap + PrefixSum
    # Approach :  
        # Idea: 
           # pastPrefixSum (需要剪掉的部分) = currentSum (現在累積多少) - target (目標要留多少)
           # 只要 pastPrefixSum 存在於 HashMap中，代表移除過去總和pastPrefixSum，讓剩下的子陣列和 = target！
           # count += hashMap[pastPrefixSum], 代表過去總和連續加到幾個不同位置都會等於pastPrefixSum
        # Use HashMap to record past_prefix_sum frequency
        # Use an O(1) HashMap to traverse array to check if diff(currentSum - target) euqals prefixSum and  diff exists before , then perform following actions
from typing import List
class Solution:
   def subarraySum(self, nums:List[int],target:int)->List[int]:
        hashMap = {0:1} # {past_prefix_sum: frequency}, （代表還沒開始加之前，總和是 0，出現了 1 次）
        count = 0
        currentSum = 0
        for i in range(len(nums)):
            currentSum += nums[i]
            diff = currentSum - target # diff = 我們需要剪掉的部分
            if diff in hashMap:
                count += hashMap[diff] # if hashMap[diff] = 2, 代表有2個past_prefix_sum 都會 等於 diff value
            hashMap[currentSum] = hashMap.get(currentSum,0)+1
        return count

# Time complexity: O(N) ... Traverse size N Array
# Space complexity:  O(N)....create size N HashMap

def test():
    sol = Solution()
    nums = [1,2,3,3]
    k=2
    result = sol.subarraySum(nums,k)
    print(f"Result:{result}")
if __name__ == "__main__":
    test()






            



