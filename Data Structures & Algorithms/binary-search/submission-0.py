class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Step 1: initialization
        left = 0
        right = len(nums) -1
        # Step 2: While Loop
        while left <= right:
        # Step 3: Move Mid +1/ -1
        # Step 4 : return -1
            mid = (left + right) //2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid -1
        return -1

    #Time Complexity: O(logN) .... Since its divided by h times, 2^h = n, h = logN
    #Space Complexity: O(1)... We didn't create extra variable or data structure

            




        

        
        