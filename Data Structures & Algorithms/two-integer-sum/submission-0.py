class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Step 1:  Initiate a map, store the key-value pair
        HashMap = {}
        #Step 2:  Iterate over array
        for i in range(len(nums)):
            current_num = nums[i]
            #Step2-1: if element shows up before, do stuff
            #Step2-2: Add the element to the Map
            if current_num in HashMap:
                return [HashMap[current_num],i]
            complement = target - current_num
            HashMap[complement] = i
        return []
        