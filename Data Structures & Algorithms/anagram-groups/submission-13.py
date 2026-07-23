"""
 OOD: No
 Constraints: No
 input : List[str]
 output : List[List[str]]
"""
# Brute Force: 
    # Anargram - Sort each string as hashmap key for grouping -> O(N* KLogK)
        # N : size N array, how many strings(how many keys)
        # K : length of a single string, how many character
    # Tricks
        # If hashmap's key contains multiple value: use defaultdict(list)
        # "".join(list) will make a list into a single string. Since sorted(string) will return a list
        # list(res.values()) convert collection to list
from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) ->List[List[str]]:
        hashMap = defaultdict(list)
        for string in strs:
            sorted_string = "".join(sorted(string))
            hashMap[sorted_string].append(string)
        return list(hashMap.values())

# Optimal Soltion:
    # Goal : O(N^2) / O(NlogN) -> O(N)
    # Keyword : “Two Sum", "Duplicate", "Frequency count", "Matching pairs", "Anagrams" -> Basic HashMap
    # Approach:  Use an O(1) HashMap to traverse array to check if a Key or Value exists before , then perform following actions
    # Tricks
        # If hashmap's key contains multiple value: use defaultdict(list)
        # If you need to group by multuple same anagram -> you don't need to sort each string(OKlogK) -> build count array with 26 alphabet as a key(O(K))
        # Hashmap's key cannot be list, we should convert it to tuple
        
class Solution:
    def groupAnagrams(self,strs:List[str])->List[List[str]]:
        hashMap = defaultdict(list)
        for string in strs:
            count = [0] *26
            for char in string:
                count[ord(char)-ord('a')] += 1
            hashMap[tuple(count)].append(string)
        return list(hashMap.values())

# Time complexity: O(N*K)
    # N : Traverse size N array, how many strings(how many keys)
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






