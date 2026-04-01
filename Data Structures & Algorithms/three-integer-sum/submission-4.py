class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 題型Keyword: “Target sum >=3” -> Two Pointers - Target Sum >=3
        # 腦中圖像:  A fixed pointer combined with two opposite pointers closing in.
        # 動作記憶法 - 3個步驟 
        # Step 1: Sort the array for two pointer technique
        nums.sort()
        res = []
        # Step 2: Traverse the array to fix the first element.
        for i, value in enumerate(nums):
            # 2-1: Skip the same value to avoid duplicate triplets in the result.
            if i > 0 and value == nums[i - 1]:
                continue
            # 2-2: Standard Two-Pointer approach for the remaining part of the array.
            # Step 1: Initialize pointers at both ends of the array.
            l, r = i + 1, len(nums) - 1
            # Step 2: Traverse the array: while left< right
            while l < r:
                # Step 2-1: Check the current state and shift pointers
                current_sum = value + nums[l] + nums[r]
                if current_sum < 0:
                    l += 1 
                elif current_sum > 0:
                    r -= 1 
                # Step 2-2: Append to the result and  Move the left pointer to find the next unique pair
                else:
                    res.append([value, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        # Step3 : Return the result 
        return res
# Time complexity: O(NlogN) ...sort the array
    # Traverse the array ... O(N)
# Space complexity:  O(1)....create constant variable
def test():
    sol = Solution()
    result = sol.threeSum([-1,0,1,2,-1,-4])
    print(f"Result: {result})")
test()


