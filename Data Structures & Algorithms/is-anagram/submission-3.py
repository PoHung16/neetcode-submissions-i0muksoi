class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Keyword : “Two Sum", "Duplicate detection", "Frequency count", "Matching pairs", "Anagrams" -> Basic HashMap
        # Image : Imagine an instant-lookup Map where you check if a Key or Value exists before , if not add it into map
        # 3-Step Flow
        #Step 1:  Initialize a map, store the key-value pair
        #Step 2: Traverse the Array to  check if a  a Key or Value exists before, if not add it into map
        #Step 3: Return the result
        hashMaps = {}
        hashMapt = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            hashMaps[s[i]] = hashMaps.get(s[i],0) +1
            hashMapt[t[i]] = hashMapt.get(t[i],0) +1
        return hashMaps == hashMapt
# Time complexity: O(N) ... Traverse size N Array
# Space complexity:  O(N)....create size N Array
def test():
    sol = Solution()
    s = "racecar"
    t = "carrace"
    result = sol.isAnagram(s,t)
    print(f"Result:{result}")




        