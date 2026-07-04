"""
 OOD: Yes
    #  A.Clarify the goal: encode and decode a list of string
    #  B.Decide the data strucure
        # Encode: Start with empty list, traverse the string and write its size and “#” and string itself, Then join the list at the end
        # Decode : Two-pointer & while loop to locate delimiters and slice segments.
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
    # Encode : Start with empty list, traverse the string and write its size and “#” and string itself, Then join the list at the end
    # Decode : Two-pointer & while loop to locate delimiters and slice segments.

from typing import List
class Solution:
    def encode(self,strs:List[str])->str:
        encoded_string_list = []
        for string in strs:
            encoded_string_list.append(f"{len(string)}#{string}")
        encoded_string = "".join(encoded_string_list)
        return encoded_string
    # Time Complexity : O(N)...traverse size N array (N is the total number of character)
    # Space Complexity: O(N)....create size N string (N is the total number of character)

    #5#abcde
    def decode(self, string: str) -> List[str]:
        i = 0  # First pointer to trace the index of the string 
        res = []
        while i < len(string):
            j = i # Second pointer to trace the position of delimeter & slice segment
            while string[j] != "#":
                j += 1
            length = int(string[i:j])
            start = j + 1
            end = start + length
            res.append(string[start:end])
            i = end
        return res
        # Time Complexity : O(N)...traverse size N array (N is the total number of character)
        # Space Complexity: O(N)....create size N res list (N is the total number of character)

def test():
    sol = Solution()
    input2 = ["#", "4#code", " ", ""]
    encoded = sol.encode(input2)
    decoded = sol.decode(encoded)
    print(f"Result: {input2} -> Encoded:{encoded} -> Decoded:{decoded}")

if __name__ == "__main__":
    test()