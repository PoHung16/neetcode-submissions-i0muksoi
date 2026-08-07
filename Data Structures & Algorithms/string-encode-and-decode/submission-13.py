"""
 OOD: Yes
    #  A.Clarify the goal: encode and decode a list of string
    #  B.Decide the data strucure
        # Encode: Start with empty list -> traverse the string list -> write its size and “#” and string itself -> Then append to the empty list -> join the list to single string
        # Decode :  Two-pointer & while loop to locate each string start index + locate delimiters & slice segment
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
# Approach : Think of a shipping label. Before each item, you write its size and “#”  
    # Encode : Start with empty list -> traverse the string list -> write its size and “#” and string itself -> Then append to the empty list -> join the list to single string
    # Decode : Two-pointer & while loop to locate each string start index + locate delimiters & slice segment
# Tricks
        # "".join(list) will make a list into a single string.
from typing import List
class Solution:
    def encode(self,strs: List[str])->str:
        empty_list = [] 
        for string in strs:
            encoded_string=f"{len(string)}#{string}"
            empty_list.append(encoded_string)
        res = "".join(empty_list)
        return res

    # Time Complexity : O(N)...traverse size N array (N is the total number of character)
    # Space Complexity: O(N)....create size N string (N is the total number of character)

    #5#abcde
    def decode(self, string:str)->List[str]:
        res = []
        i = 0 # locate each string start index
        while i < len(string):
            j = i # locate each string delimiters 
            while string[j]!="#":
                j+=1
            length = int(string[i:j])
            start = j+1
            end = start+length
            substring = string[start:end]
            res.append(substring)
            i = end
        return res

        # Time Complexity : O(N)...traverse size N array (N is the total number of character)
        # Space Complexity: O(N)....create size N res list (N is the total number of character)

def test():
    sol = Solution()
    input2 = ["Hello","World"]
    encoded = sol.encode(input2)
    decoded = sol.decode(encoded)
    print(f"Result: {input2} -> Encoded:{encoded} -> Decoded:{decoded}")

if __name__ == "__main__":
    test()