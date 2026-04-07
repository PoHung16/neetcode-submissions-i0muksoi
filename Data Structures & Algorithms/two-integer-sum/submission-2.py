class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Keyword : “Two Sum", "Duplicate detection", "Frequency count", "Matching pairs", "Anagrams" -> Basic HashMap
        # Image : Imagine an instant-lookup Map where you check if a Key or Value exists before , if not add it into map
        # 3-Step Flow
        #Step 1:  Initialize a map, store the key-value pair
        #Step 2:  Traverse the Array to  check if a  a Key or Value exists before, if not add it into map
        #Step 3: Return the result
        hashMap = {} # num, index
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashMap:
                return [hashMap[complement],i]    
            hashMap[nums[i]] = i                
        return []
# Time complexity: O(N) ... Traverse size N Array
# Space complexity:  O(N)....create size N Array
def test():
    sol = Solution()
    nums = [3,4,5,6]
    target = 7
    result = sol.hasduplicate(nums,target)
    print(f"Result:{result}")