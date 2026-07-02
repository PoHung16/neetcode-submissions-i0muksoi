"""
 OOD: Yes
    #  A.Clarify the goal: encode and decode a list of string
    #  B.Decide the data strucure
        # Encode: Implement it with empty list, traverse the string and write its size and “#” and string itself, Then join at the end
        # Decode : Decode the string using a two-pointer while loop to locate delimiters and slice segments.
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
# Image : Think of a shipping label. Before each item, you write its size and “#”  
    # Encode : Implement it with empty list, traverse the string and write its size and “#” and string itself, Then join at the end
    # Decode : Decode the string using a two-pointer while loop to locate delimiters and slice segments.

from typing import List
class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_str = []
        for string in strs:
            encoded_str.append(f"{len(string)}#{string}")
        res = "".join(encoded_str)
        return res

    # Time Complexity : O(N)...traverse size N array (N is the total number of character)
    # Space Complexity: O(N)....create size N string (N is the total number of character)

    #5#abcde
    def decode(self, string: str) -> List[str]:
        # First pointer to trace the index of the string 
        i = 0
        res = []
        while i < len(string):
            j = i # Second pointer to trace the position of delimeter & slice segment
            while string[j] != "#":
                j+=1
            length = int(string[i:j])
            start = j+1
            end = j+1+length
            res.append(string[start:end])
            i = end
        return res
        # Time Complexity : O(N)...traverse size N array (N is the total number of character)
        # Space Complexity: O(N)....create size N res list (N is the total number of character)

def test():
    sol = Solution()
    input2 = ["#", "4#code", " ", ""]
    encoded2 = sol.encode(input2)
    decoded2 = sol.decode(encoded2)
    print(f"\nTest 2 - Input: {input2}")
    print(f"Encoded: {encoded2}")
    print(f"Decoded: {decoded2}")

if __name__ == "__main__":
    test()

        