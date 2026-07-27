"""
 OOD: No
 Constraints: Yes
 input : List[int],int
 output : int
"""
# Brute Force: 
    # Array - Traverse the array to check every element to see if there's match -> O(N)
class Solution:
    def search(self,nums:List[int],target:int)->int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1

# Optimal Solution
    # Goal: make O(N) search -> O(logN)
    # Keyword:  "LogN complexity" or “Sorted Array " or "Sorted 2D matrix" or "Search in rotated array" -> Basic Binary Search
    # Approach: 
        # 1. Two pointer to Get "Mid" to decide search on which side. Diffrent from 2 pointer, while l<=r ,remember "=" to ensure the loop still runs when the search range shrinks to a single element
    
class Solution:
    def search(self,nums:List[int],target:int)->int:
        l,r = 0, len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid -1
        return -1

# Time Complexity: O(logN) .... Since its divided by h times, 2^h = n, h = logN
# Space Complexity: O(1)... We didn't create extra variable or data structure       

def test():
    sol = Solution()
    nums = [-1,0,2,4,6,8]
    target = 4
    result = sol.search(nums,target)
    print(f"Result:{result}")

if __name__ == "__main__":
    test()


    




        

        
        