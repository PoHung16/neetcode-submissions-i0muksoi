"""
 OOD: No
 Constraints: No
 input : str
 output : boolean
"""
# Keywork : Two Sum -> but solution must use O(1) additional space -> cannot use hashmap
# Keyword : “Palindrome",”Target Sum”,“maximum area of water”  -> Basic Two pointer 
# Image : Two pointer Shrink from both ends to find the perfect fit
# Tricks:
    # Sorting is a great way to prep your data before applying a two-pointer approach.
from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0 , len(numbers)-1
        while l < r:
            current_sum = numbers[l] + numbers[r]
            if current_sum < target:
                l+=1
            elif current_sum > target:
                r-=1
            else:
                return [l+1,r+1]
        return []

def test():
    sol = Solution()
    result = sol.twoSum([1,2,3,4],3)
    print(f"Result: {result})")
if __name__ == "__main__":
    test()

# Time complexity: O(N) ...traverse size N array
# Space complexity:  O(1)....create constant variable
