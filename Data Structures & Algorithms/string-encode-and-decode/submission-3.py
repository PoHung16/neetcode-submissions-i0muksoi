# A. Clarify the goal: Pack many strings into one string so you can send it over the network, then unpack it later without losing any data.
# B. Decide the data strucure
    #Encode: Use a String to join them.
    #Decode: Use a List to store the recovered strings.
# C. Implement constructor and method

# Keyword : Keyword : “Decode & Encode String” - String Parsing 
# Image: Imagine Tagging. Think of a shipping label. Before each item, you write its size and “#”
# Workflow- Encode 
    #Step 1:  For each string, join: [Length] + [#] + [String].
#Workflow- Decode
    #Step 1: Traverse the string to read the size before "#" and string after "#" with 2 pointer
class Solution:
    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            # Join Length + # + String
            res.append(f"{len(s)}#{s}")
        # Join into one final string
        return "".join(res)
    # Time complexity: O(N) ... Traverse size N Array
    # Space complexity:  O(N)....create size N Strings
    def decode(self, string:str) -> List[str]:
        res = []
        i = 0 # i is searching for length size
        while i < len(string):
            j = i # j is searching for delimeter
            while string[j] != "#":
                j += 1
            length = int(string[i:j])
            word = string[j+1: j+1 +length]
            res.append(word)
            i = j + 1 + length
        return res
    # Time complexity: O(N) ... Traverse size N Array
    # Space complexity:  O(N)....create size N String List

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

        