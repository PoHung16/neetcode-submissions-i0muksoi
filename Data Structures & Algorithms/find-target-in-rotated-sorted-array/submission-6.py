class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Keyword : Search in Rotated Sorted Array -> Binary Search :  Search in Rotated Sorted Array 
        # Image : Check which side is a normal slope and perform Binary Search to find the target
        # 3-Step Flow
        l, r = 0, len(nums)-1
        res = -1 #res to record our output

        while l<=r:
            # Step 2-1: Get the value
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            # Step 2-2 : Check which half is sorted perform binary search
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid -1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid -1
        return -1
# Time complexity: O(LogN) ... Binary Search...Tree height
# Space complexity:  O(1)....create constant variable               





