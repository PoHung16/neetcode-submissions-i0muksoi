"""
 OOD: No
 Constraints: No
 input : String, String
 output : bool
"""
# Brute Force: 
    # String: For loop to Traverse all substrings of s2  with the length of s1, sort them both, to see if there's identical string -> O( (n2-n1) * N1log(N1))

class Solution:
    def checkInclusion(self, s1:str, s2:str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        if n1 > n2:
            return False
        sorted_s1 = sorted(s1)
        # startIndex + n1-1 (往後數n1-1個字元)= last index (n2-1)
        # -> startIndex + n1-1 = n2 -1
        # -> startIndex = n2-n1 (最後只能在這)
        for i in range(n2-n1+1):
            substring = s2[i:i+n1]
            sorted_substring = sorted(substring)
            if sorted_substring == sorted_s1:
                return True
        return False


# Optimal Solution
    # Goal: O(N^2) -> O(N)
    # Keyword:  “Permutation in String" -> Sliding Window (Fixed Size) -edge case
    # Approach: 
        # 1. Build 2 state variable map to record window state, fill in the state map in advance
        # 2. Expand from the right with fixed range,
        # 3. Update the state variable(left & right)  then check if current window matches s1's frequency map
        
    
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # edge case
        n1 = len(s1)
        n2 = len(s2)
        if n1 > n2 or not n1:
            return False
        hashMapS1 = {}
        hashMapS2 = {}
        for i in range(n1):
            hashMapS1[s1[i]] = hashMapS1.get(s1[i],0) + 1
            hashMapS2[s2[i]] = hashMapS2.get(s2[i],0) + 1

        if hashMapS1 == hashMapS2:
            return True

        for right in range(n1,n2):
            left = right - n1
            hashMapS2[s2[right]] = hashMapS2.get(s2[right],0) + 1
            hashMapS2[s2[left]] -= 1
            if hashMapS2[s2[left]]==0:
                del hashMapS2[s2[left]]
            if hashMapS1 == hashMapS2:
                return True
            
        return False

    
# Time complexity: O(N2) ...traverse size N2 array, N2 is the length of s2 (ON1+N2-N1) = O(N2)
# Space complexity:  O(1)...create size 26 hashMap. 

def test():
    sol = Solution()
    result = sol.checkInclusion("abc","lecabee")
    print(f"Result: {result}")
if __name__ == "__main__":
    test()





