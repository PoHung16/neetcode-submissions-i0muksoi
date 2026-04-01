class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 題型Keyword: “Palindrome” , “Sorted Array”, “Remove duplicates”, “Target Sum <=2”, “maximum area of water” -> Standard Two pointer 
        # 腦中圖像: Two opposite pointers closing in
        # 動作記憶法 - 3個步驟 
        # Step1:  Initialize pointers at both ends of the array.
        l, r = 0, len(numbers)-1
        # Step2: Traverse the array : while left< right
        while l < r:
            curSum = numbers[l] + numbers[r]
            if curSum < target:
                l+=1
            elif curSum > target:
                r-=1
            else:
                return [l+1,r+1]
        # Since there's exactly one valid solution. we don't need to skip the same element
        # Step3 : Return the result 
        return []

# Time complexity: O(N) ...traverse size N array
# Space complexity:  O(1)....create constant variable
def test():
    sol = Solution()
    result = sol.twoSum([1,2,3,4],3)
    print(f"Result: {result})")
test()


