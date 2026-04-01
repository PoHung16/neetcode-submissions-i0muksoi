class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Step 1:  Initiate a map, store the key-value pair
        seenMap = {}
        #Step 2:  Iterate over array
        for num in nums:
            #Step2-1: if element shows up before, return True
            if num in seenMap:
                return True
            #2-2Add the element to the Map
            seenMap[num] = True
        #Step2-3: 最終檢查
        return False