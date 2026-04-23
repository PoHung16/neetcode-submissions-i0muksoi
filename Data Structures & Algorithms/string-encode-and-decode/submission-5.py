"""
 OOD: Yes- As you can see in Example
    #  A.Clarify the goal: encode and decode a list of string
    #  B.Decide the data strucure
        #Encode: Implement it with join , list 
        #Decode: Implement it with while loop + 2 pointer to trace delimeter position and length of next string
    # Implement constructor and method
 Constraints: No
 input : 
    #List[str]
    #str
 output : 
    #str
    #List[str]
"""
# Keyword:  “Decode & Encode String” - String Parsing 
# Image : Think of a shipping label. Before each item, you write its size and “#” . 
    # Encode : Implement it with join , list 
    # Decode : Implement it with while loop + 2 pointer to trace delimeter position and length of next string
from typing import List
class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_string = []
        for s in strs:
            encoded_string.append(f"{len(s)}#{s}")
        return "".join(encoded_string)
        # Time Complexity : O(N)...traverse size N array (N is the number of character)
        # Space Complexity: O(N)....create size N string (N is the number of character)

    def decode(self, string: str) -> List[str]:
        res = []
        i = 0
        while i< len(string):
            j = i
            while string[j] != "#":
                j+=1
            length = int(string[i:j])
            start = j+1
            end = j+1+length
            res.append(string[start:end])
            i = end
        return res
        # Time Complexity : O(N)...traverse size N array (N is the number of character)
        # Space Complexity: O(N)....create size N res list (N is the number of character)

def test():
    sol = Solution()
    # Test Case 2: Special characters (The real challenge!)
    input2 = ["#", "4#code", " ", ""]
    encoded2 = sol.encode(input2)
    decoded2 = sol.decode(encoded2)
    print(f"\nTest 2 - Input: {input2}")
    print(f"Test 2 - Encoded: '{encoded2}'")
    print(f"Test 2 - Success: {input2 == decoded2}")

if __name__ == "__main__":
    test()

        