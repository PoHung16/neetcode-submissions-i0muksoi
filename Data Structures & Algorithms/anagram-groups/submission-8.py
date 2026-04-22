"""
 OOD: No
 Constraints: No
 input : List[str]
 output : List[List[str]]
"""
# Keyword : “Two Sum", "Duplicate", "Frequency count", "Matching pairs", "Anagrams" -> Basic HashMap
# Image : Imagine an instant-lookup Map Traverse an array to check if a Key or Value exists before , then perform following actions
# Tricks: 
    # if hashmap's key contains multiple value: use defaultdict(list)
    # if you need to count the same anagram , can build count array with 26 alphabet
    # hashmap's key cannot be list, we should convert it to tuple

from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str])->List[List[str]]:
        hashMap = defaultdict(list)
        for string in strs:
            count = [0]* 26
            for char in string:
                count[ord(char)-ord('a')]+=1
            hashMap[tuple(count)].append(string)
        return list(hashMap.values()) # collections -> list

def test():
    sol = Solution()
    strs = ["act","pots","tops","cat","stop","hat"]
    result = sol.groupAnagrams(strs)
    print(f"Result:{result}")

if __name__ == "__main__":
    test()
        
# Time complexity: O(N*L)
    # Traverse Size N Array, and nested traverse the string length L
# Space complexity: O(N*L)
    # Create size N*L hashMap , N is the size of the input, L is the string length
    # Create size 26 count array * N = O(1) *N 
