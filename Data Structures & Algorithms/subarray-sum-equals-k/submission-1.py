"""
 OOD: No
 Constraints: No
 input : List[int], int
 output : int
"""
# Brute Force: 
    # Scan every possible start and end position using nested loop to calculate if subarray sums match target -> O(N^2)
class Solution:
    def subarraySum(self, nums:List[int],target:int)->List[int]:
        count = 0
        for i in range(len(nums)):
            currentSum = 0
            for j in range(i,len(nums)):
                currentSum += nums[j]
                if currentSum==target:
                    count+=1
        return count

# Optimal Soltion:
    # Keyword : "Contiguous Subarray + Negative Numbers" ->Prefix Sum + HashMap.
    # Keyword : “Except Self" -> PrefixProduct
    # Tricks: 
        # Am I repeating calculations? (e.g., re-adding the same subarray elements over and over). -> Prefix Sums
        # Am I looking up data inefficiently? (e.g., scanning an entire array linearly just to find if a number exists)-> HashMap

class Solution:
   def subarraySum(self, nums:List[int],target:int)->List[int]:
        count = 0
        hashMap = {0: 1} # {prefix_sum: frequency}
        currentSum = 0
        for i in range(len(nums)):
            currentSum += nums[i]
            diff = currentSum - target # if diff equals prefix_sum
            if diff in hashMap: # Check how many times prefix sum shows up
                count += hashMap[diff]
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






