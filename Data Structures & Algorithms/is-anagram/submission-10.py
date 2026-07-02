"""
OOD : X
Contraints: X
Input: String, String
Output: boolean
"""
# Brute Force: 
    # Sort both strings and check if they are identical. -> O(NlogN)
class Solution:
    def isAnagram(self,s:str,t:str)->bool:
        return sorted(s) == sorted(t)
# Optimal Solution
    # Keyword : “Two Sum", "Duplicate", "Frequency count", "Matching pairs", "Anagrams" -> Basic HashMap
    # Approach:  Use an O(1) HashMap to traverse array to check if a Key or Value exists before , then perform following actions
    # Tricks:
        # If there are 2 input Strings to match , we build 2 hashMap to compare anagrams

class Solution:
    def isAnagram(self,s:str,t:str)->bool:
        if len(s)!=len(t):
            return False
        hashMapS = {}
        hashMapT = {}
        for i in range(len(s)):
            hashMapS[s[i]] = hashMapS.get(s[i],0)+ 1
            hashMapT[t[i]] = hashMapT.get(t[i],0)+ 1
        return hashMapS==hashMapT

# Time complexity: O(N) ... Traverse size N Array *2
# Space complexity:  O(N)....create 2 size N HashMap

def test():
    sol = Solution()
    s = "racecar"
    t = "carrace"
    result = sol.isAnagram(s,t)
    print(f"Result: {result}")
if __name__ == "__main__":
    test()








