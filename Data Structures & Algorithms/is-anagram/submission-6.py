"""
OOD : X
Contraints: X
Input: String, String
Output: boolean
"""
# Keyword : “Two Sum", "Duplicate", "Frequency count", "Matching pairs", "Anagrams" -> Basic HashMap
# Image : Imagine an instant-lookup Map Traverse an array to check if a Key or Value exists before , then perform following actions
class Solution:
    def isAnagram(self,s:str,t:str)->bool:
        if len(s) != len(t):
            return False
        hashMapS = {}
        hashMapT = {}
        for i in range(len(s)):
            hashMapS[s[i]] =hashMapS.get(s[i],0) + 1
            hashMapT[t[i]] =hashMapT.get(t[i],0) + 1
        return hashMapS == hashMapT
def test():
    sol = Solution()
    s = "racecar"
    t = "carrace"
    result = sol.isAnagram(s,t)
    print(f"Result:{result}")
if __name__ == "__main__":
    test()

# Time complexity: O(N) ... Traverse size N Array
# Space complexity:  O(N)....create 2 size N HashMap

