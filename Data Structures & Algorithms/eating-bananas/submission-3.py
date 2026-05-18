"""
 OOD: No
 Constraints: No
 input : List[int],int
 output : int
"""
# Keyword : "Find the minimum or maximum value to pass a test.">  Binary Search on Answer 題型
# Image :  Traverse the array with l, r pointer
# Tricks :  
   # A. The squeeze use "while l <= r” ensures the loop still runs when the search range shrinks to a single element.
   # B.  put l & r on the lowest and highest possible answers. Use mid as a test answer. If mid passes, try a smaller answer on the left. If it fails, look for a larger answer on the right.

from typing import List
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        best_ans = r
        while l<=r:
            mid = (l+r)//2
            total_time = 0
            for p in piles:
                total_time += (p + mid - 1) // mid
            if total_time <= h:
                best_ans = mid
                r = mid - 1#找更慢
            else:
                l = mid + 1 #找更快
        return best_ans


def test():
    sol = Solution()
    piles = [1,4,3,2]
    h = 9
    result = sol.minEatingSpeed(piles,h)
    print(f"Result:{result}")

if __name__ == "__main__":
    test()

# Time Complexity: O(NlogM) .... M is the search range on the answer,  N is the total number of piles in the input array.
    # Everytime we perform binary search, we will need to traverse size N array to calculate hours_needed
# Space Complexity: O(1)... We didn't create extra variable or data structure       



