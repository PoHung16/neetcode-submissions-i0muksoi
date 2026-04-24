"""
 OOD: No
 Constraints: No
 input : List[int]
 output : int
"""
 # Keyword : “Palindrome", "Target Sum", “maximum area of water”  -> Basic Two pointer 
 # Image : Two pointer Shrink from both ends to find the perfect fit
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res
def test():
    sol = Solution()
    result = sol.maxArea([1,7,2,5,4,7,3,6])
    print(f"Result: {result})")
if __name__ == "__main__":
    test()
# Time complexity: O(N) ...traverse size N array
# Space complexity:  O(1)....create constant variable




