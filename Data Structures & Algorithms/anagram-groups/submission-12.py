"""
 OOD: No
 Constraints: No
 input : List[str]
 output : List[List[str]]
"""
# Brute Force: 
    # Sort each string to use as a hash map key for grouping -> O(N * KlogK)
        # N : size N array, how many strings
        # K : length of a single string, how many character
    # Tricks
        # If hashmap's key contains multiple value: use defaultdict(list)
        # "".join(list) will make a list into string. Since sorted(string) will return a list
        # list(res.values()) convert collection to list
from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self,strs:List[str])->List[List[str]]:
        res = defaultdict(list)
        for string in strs:
            sorted_string = "".join(sorted(string))
            res[sorted_string].append(sorted_string)
        return list(res.values())


# Optimal Soltion:
    # Keyword : “Two Sum", "Duplicate", "Frequency count", "Matching pairs", "Anagrams" -> Basic HashMap
    # Approach:  Use an O(1) HashMap to traverse array to check if a Key or Value exists before , then perform following actions
    # Tricks
        # If hashmap's key contains multiple value: use defaultdict(list)
        # If you need to group by multuple same anagram -> Character Count as Key Technique -> build count array with 26 alphabet
        # Hashmap's key cannot be list, we should convert it to tuple
        
class Solution:
    def groupAnagrams(self,strs:List[str])->List[List[str]]:
        hashMap = defaultdict(list)
        for string in strs:
            count = [0]*26
            for char in string:
                count[ord(char)-ord('a')] += 1
            hashMap[tuple(count)].append(string)
        return list(hashMap.values())

# Time complexity: O(N*K)
    # N : Traverse size N array, how many strings
    # K : Traverse length of a single string, how many character
# Space complexity: O(N*K)
    # Value: we have N different string value, each have K character
    # Keys: we have N different Keys value, each key size 26: O(26*N)
       
def test():
    sol = Solution()
    strs = ["act","pots","tops","cat","stop","hat"]
    result = sol.groupAnagrams(strs)
    print(f"result:{result}")
if __name__ == "__main__":
    test()


