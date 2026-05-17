"""
 OOD: No
 Constraints: Yes
 input : List[int],int
 output : int
"""
# Keyword : "Find the minimum or maximum value to pass a test.">  Binary Search on Answer 題型
# Image :  Traverse the array with l, r pointer, put l & r on the lowest and highest possible answers. Use mid as a test answer. If mid passes, try a smaller answer on the left. If it fails, look for a larger answer on the right.
# Tricks :  
    # use “=”, "l <= r” ensures the loop still runs when the search range shrinks to a single element.


from typing import List
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        best_ans = r 
        while l <= r:
            mid = (l + r) // 2  # Test this specific answer (speed) 
            # Check feasibility : 
            # Way1: math.ceil(A/B) ->會變成浮點數
            # Way2: (A+B-1)//B
            hours_needed = 0
            for banana in piles:
                hours_needed += (banana+mid-1)//mid

            if hours_needed <= h:
                best_ans = mid  # This works! Save it.
                r = mid - 1 #Look left for a smaller speed.
            else:
                l = mid+1 #  Too slow! Look right for a faster speed.
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



