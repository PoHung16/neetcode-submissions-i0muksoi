"""
 OOD: No
 Constraints: No
 input : str
 output : boolean
"""
# Brute Force: 
    # Palindrome - filter non-alphanumeric characters and converting it to lowercase, then check if this new string equals its reverse. -> O(N)
class Solution:
    def isPalindrome(self,s: str)->bool:
        filtered_string_list = [c.lower() for c in s if c.isalnum()]
        return filtered_string_list == filtered_string_list[::-1]

# Optimal Solution
    # Goal : To save space complexity from O(N)-> O(1)
    # Keyword:  “Palindrome",”Target Sum”,“get maxium from Array Operation”  -> Basic Two pointer 
    # Approach: Two pointer Shrink from both ends to find the perfect fit
class Solution:
    def isPalindrome(self,s: str)->bool:
        l, r = 0 , len(s)-1
        while l < r: #stops when equal, no need for "="
            if not s[l].isalnum():
                l+=1
            elif not s[r].isalnum():
                r-=1
            else:
                if s[l].lower() != s[r].lower():
                    return False
                else:
                    l+=1
                    r-=1
        return True

# Time complexity: O(N) ...traverse size N array
# Space complexity:  O(1)....create constant variable

def test():
    sol = Solution()
    result = sol.isPalindrome("Was it a car or a cat I saw?")
    print(f"result:{result}")

if __name__ == "__main__":
    test()




