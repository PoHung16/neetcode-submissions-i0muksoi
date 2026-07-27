"""
 OOD: No
 Constraints: No
 input : List[int]
 output : List[List[int]]
"""
# Brute Force: 
    # Array - Use triple nested Loop to loop through every possible pair of numbers to see if each pair's sum equal, then we sorted triplet as set() key to make sure there's no duplicate  ->O(N^3 * 3Log3)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = tuple(sorted([nums[i],nums[j],nums[k]]))  # convert list to tuple for set() key
                        res.add(triplet)
        return [list(triplet) for triplet in res] # convert tuple back to list

# Optimal Solution
    # Goal : O(N^3)-> O(N^2), Two pointer technique : O(N^2)->O(N)
    # Keyword:  “Palindrome",”Target Sum”,“get maxium from Array Operation”  -> Basic Two pointer 
    # Approach: Two pointer Shrink from both ends to find the perfect fit
    # Tricks:
        # Sorting is a great way to prep your data before applying a two-pointer approach.
        # If the question state "Should not contain any duplicate" : 
            # To fast-forward duplicates, check boundary first, then peek if the next one is a twin.
                # inside for loop: if "i>0" and nums[i-1] == nums[i]: continue -> next iteration  for loop
                # inside while loop: while "l<r" and nums[l-1] == nums[l], l+=1 -> next iteration for while loop 
                # inside while loop: while "i+1 < len(nums)" and nums[i+1] == nums[i], i+=1 -> next iteration for while loop 
from typing import List
class Solution:
    def threeSum(self, nums:List[int])-> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i-1] == nums[i]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                currentSum = nums[i] + nums[l] + nums[r]
                if currentSum < 0:
                    l+=1
                elif currentSum > 0:
                    r-=1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    while l <r and nums[l-1] == nums[l]:
                        l+=1
        return res

# Time complexity: O(N^2) 
    # Sort the array.... O(NlogN)
    # Nested loop to Traverse the array ... O(N^2)
# Space complexity:  O(M)....space for the output list. Where m is the number of triplets 

def test():
    sol = Solution()
    result = sol.threeSum([-1,0,1,2,-1,-4])
    print(f"Result: {result})")
if __name__ == "__main__":
    test()







