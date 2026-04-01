class Solution:
    def findMin(self, nums:List[int]) -> int:
        # Keyword : Search in Rotated Sorted Array -> Binary Search :  Search in Rotated Sorted Array 
        # Image : Check which side is a normal slope to find where the big drop-off is, the minimum value is there
        # 3-Step Flow
        # Step 1: Initialize left, right pointer
        l, r = 0, len(nums)-1
        res = nums[0]  #res to record our output
        # Step 2: Traverse the array with l,r pointer (Perform Binary Search)
        while l <=r:
            # Step 2-1: Get the value - if the array is already sorted
            if nums[l] < nums[r]:
                res = min(res,nums[l]) # the minimum might be on the mid point
                return res
            mid = (l+r) //2
            res = min(res,nums[mid]) # We need to record the value at mid before we shrink the search space, Since the mid spot might be the minimum we're looking for
            # Step 2-2 : Check which half is sorted and jump to the other side.
            if nums[l] <= nums[mid]:
                l = mid+1  # Left side is a normal slope, so the drop-off is to the right.
            else:
                r = mid -1
        #Step 3: Return result
        return res
# min(array) will cost O(N) since it traverse an array to make comparision
# Time complexity: O(LogN) ... Binary Search...Tree height
# Space complexity:  O(1)....create constant variable
def test():
    sol = Solution()
    result = sol.findMin([3,4,5,6,1,2])
    print(f"Result: {result})")
test()
    
