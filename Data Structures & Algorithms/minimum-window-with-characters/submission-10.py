"""
 OOD: No
 Constraints: No
 input : String, String
 output : String
"""
# Keyword : “A Consecutive sequence”, "Substring"  -> Sliding Window (Variable Size) - edge case
# Image :  A state window that expands until it meets a condition, then shrinks from the left, usually implement with statemap.
# Tricks:
    # Two map, if there are 2 input String to match
    # Minimum window substring:  Instead of comparing two maps (O(K)), use a 'have' variable to track unique characters that meet the frequency. This makes validation O(1).


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #ps. Edge case
        if not t or not s: 
            return ""
        target_map ={}
        for char in t:
            target_map[char] = target_map.get(char,0)+1
        window_map={}
        have, need = 0, len(target_map)
        
        start = 0
        res_range, res_len =[-1,-1],float("inf")
        
        for end in range(len(s)):
            window_map[s[end]] = window_map.get(s[end], 0) + 1
            if s[end] in target_map and window_map[s[end]] == target_map[s[end]]:
                have += 1
            while have==need:
                if end-start+1 < res_len :
                    res_len = end-start+1 
                    res_range = [start,end]
                window_map[s[start]] -= 1
                # If removing this char makes the window invalid
                if s[start] in target_map and window_map[s[start]] < target_map[s[start]]:
                    have -=1
                start+=1
        final_start, final_end = res_range
        return s[final_start : final_end+1] if res_len != float("inf") else "" 


def test():
    sol = Solution()
    result = sol.minWindow("OUZODYXAZV","XYZ")
    print(f"Result: {result}")

if __name__ == "__main__":
    test()

# Time Complexity: O(N + M) - traverse size N array, and size M array
    # N is the length of string s  to put it in map
    # M is the length of string t  to expand the window
# Space Complexity: O(K) 
    # we create total size K Map, K is the number of unique characters in s and t.
