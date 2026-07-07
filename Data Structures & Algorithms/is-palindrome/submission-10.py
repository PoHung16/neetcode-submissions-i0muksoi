"""
 OOD: No
 Constraints: No
 input : str
 output : boolean
"""
# Brute Force: 
    # Check the palindrome by filtering out non-alphanumeric characters and converting it to lowercase, then check if this new string equals its reverse. -> O(N)
class Solution:
    def isPalindrome(self,s: str)->bool:
        cleaned_string = [char.lower() for char in s if char.isalnum()]
        return cleaned_string == cleaned_string[::-1]
# Optimal Solution
    # Goal : To save space complexity from O(N)-> O(1)
    # Keyword:  “Palindrome",”Target Sum”,“maximum area of water”  -> Basic Two pointer 
    # Approach: Two pointer Shrink from both ends to find the perfect fit
class Solution:
    def isPalindrome(self,s: str)->bool:   
        l, r = 0, len(s)-1
        while l < r :
            if not s[l].isalnum():
                l+=1
            elif not s[r].isalnum():
                r-=1
            else:
                if s[l].lower() != s[r].lower():
                    return False
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



