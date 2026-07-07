"""
 OOD: No
 Constraints: No
 input : List[int]
 output : List[List[int]]
"""
# Brute Force: 
    # Use triple nested Loop to loop through every possible pair of numbers to see if each pair's sum equal  ->O(N^3)
class Solution:
    def threeSum(self, nums: List[int])-> List[List[int]]:
        res = set() # we should use set instead of [] to prevent duplicate
        for i in range(len(nums)): 
            for j in range(i+1, len(nums)): 
                for k in range(j+1, len(nums)): 
                    if nums[i] + nums[j] + nums[k] == 0:
                        # sort triplet first to ensure the key are the same  to prevent duplicate
                        triplet = tuple(sorted(nums[i],nums[j],nums[k])) # convert list to tuple for set() key
                        res.add(triplet)
        return [list(triplet) for triplet in res] # convert tuple back to list

# Optimal Solution
    # Goal : To save time complexity from O(N^3)-> O(N^2)
    # Keyword:  “Palindrome",”Target Sum”,“maximum area of water”  -> Basic Two pointer 
    # Approach: Two pointer Shrink from both ends to find the perfect fit
    # Tricks:
        # Sorting is a great way to prep your data before applying a two-pointer approach.
        # If the question state "Should not contain any duplicate" : 
            # if i>0 and nums[i-1] == nums[i]: continue -> "符合條件"continue 會跳出「這一輪」，回到 for 的開頭，
            # while l<r and nums[l-1] == nums[l]: l+=1 ，"不符合條件" 會跳出「這一次 while 迴圈」，回到 while 的開頭
class Solution:
    def threeSum(self, nums: List[int])-> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)): 
            if i>0 and nums[i-1] == nums[i]:
                continue
            l , r = i+1 , len(nums)-1
            while l < r:
                currentSum = nums[i] + nums[l] + nums[r]
                if currentSum < 0:
                    l+=1
                elif currentSum > 0:
                    r-=1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    while l<r and nums[l-1] == nums[l]:
                        l+=1
        return res

# Time complexity: O(N^2) 
    # Sort the array.... O(nlogN)
    # Nested loop to Traverse the array ... O(N^2)
# Space complexity:  O(M)....space for the output list. Where m is the number of triplets 

def test():
    sol = Solution()
    result = sol.threeSum([-1,0,1,2,-1,-4])
    print(f"Result: {result})")
if __name__ == "__main__":
    test()
