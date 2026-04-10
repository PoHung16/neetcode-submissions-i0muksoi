class Solution:
    def isAnagram(self,s:str,t:str) -> bool:
        # Keyword : “Two Sum", "Duplicate", "Frequency count", "Matching pairs", "Anagrams" -> Basic HashMap
        # Image: Imagine an instant-lookup Map where you check if a Key or Value exists before , then perform following actions
        # Workflow - 3 Steps:
        # Step 1: Initialize a map, store the key-value pair
        # Step 2: Traverse the Array to check if a Key or Value exists before,, then perform following actions
        # Step 3: Return the result
        if len(s) != len(t):
            return False
        hashMaps = {}
        hashMapt = {}
        for i in range(len(s)):
            hashMaps[s[i]] = hashMaps.get(s[i],0) + 1
            hashMapt[t[i]] = hashMapt.get(t[i],0) + 1

        return hashMaps==hashMapt
def test():
    sol = Solution()
    s = "racecar"
    t = "carrace"
    result = sol.isAnagram(s,t)
    print(f"Result:{result}")
# Time complexity: O(N) ... Traverse size N Array
# Space complexity:  O(N)....create 2 size N HashMap

