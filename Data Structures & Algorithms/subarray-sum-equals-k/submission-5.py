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
                    count += 1
                    break
        return count
# Optimal Soltion:
    # Goal: O(N^2) / O(NlogN) -> O(N)
    # Keyword: "Contiguous Subarray+ Negative Numbers"-> HashMap + PrefixSum
    # Idea:
        # A. 你一路往前走，把所有數字加總，得到現在的累積總和（currentPrefixSum） = 100塊
        # B. 你想要留 30 塊(Target) -> 你前面必須花掉 70 塊 (pastPrefixSum)
        # C. 你只要回頭問 HashMap：之前有沒有哪個時間點，我手上剛好累積 70 塊？ 我就在那時候把70塊都花掉了
            # C-1 有幾次，就代表有幾種切法可以切出剩下 30 塊的 Subarray。
    # Approach:
        # 1. Use a hashMap to record the frequency of pastPrefixSum's value, to see how many times this pastPrefixSum's value shouw up (stop at how many different index), can let subarray equals target
        # 2. Use HashMap to traverse array to  check if a Key or Value exists before , then perform following actions
        
from typing import List
class Solution:
    def subarraySum(self, nums:List[int], target:int)->List[int]:
        hashMap = {0:1} # {past_prefix_sum: frequency}, （代表還沒開始加之前，總和是 0，出現了 1 次）
        currentPrefixSum = 0
        count = 0
        for i in range(len(nums)):
            currentPrefixSum += nums[i]
            pastPrefixSum = currentPrefixSum - target
            if pastPrefixSum in hashMap:
                count += hashMap[pastPrefixSum]
            hashMap[currentPrefixSum] = hashMap.get(currentPrefixSum,0)+1
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






            














