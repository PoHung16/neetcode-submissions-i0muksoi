"""
 OOD: No
 Constraints: No
 input : List[int], int
 output : List[int]ean
"""
# Brute Force: 
    # Array - Use nested Loop to loop through every possible pair of numbers to see if each pair's sum equal  ->O(N^2)
class Solution:
    def twoSum(self, nums:List[int],target:int)-> List[int]:
        res = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    res.append([i+1,j+1])
        return []
        
# Optimal Solution
    # Goal : To save time complexity from O(N^2)-> O(N)
    # Keyword:  “Palindrome",”Target Sum”,“get maxium from Array Operationr”  -> Basic Two pointer 
    # Approach: Two pointer Shrink from both ends to find the perfect fit
    # Tricks:
        # Sorting is a great way to prep your data before applying a two-pointer approach.

class Solution:
    def twoSum(self, nums:List[int],target:int)-> List[int]:
        l, r = 0, len(nums)-1
        while l < r: # stops when equal, no need for "="
            if nums[l]+nums[r] == target:
                return[l+1,r+1]
            elif nums[l]+nums[r] < target:
                l+=1
            else:
                r-=1
        return []

# Time complexity: O(N)
    # Sort: O(NlogN)...don't need to sort, already sorted
    # Traverse size N array: O(N)

# Space complexity:  O(1)....create constant variable

def test():
    sol = Solution()
    result = sol.twoSum([1,2,3,4],3)
    print(f"Result: {result})")
if __name__ == "__main__":
    test()


