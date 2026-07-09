"""
 OOD: No
 Constraints: No
 input : List[int],int
 output : int
"""
# Brute Force: 
    # Traverse the array from minimum speed 1 up to the maximum pile size, calculating the total hours required ->O(M*N)
    # M i is the number of piles, N is the maximum number of bananas you can in a single pile. (how many times you iterate)
from typing import List
class Solution:  
    def minEatingSpeed(self,piles:List[int],h:int):
        k = 1
        while True:
            total_hours = 0
            for pile in piles:
                total_hours += (pile +k -1)//k
            if total_hours <= h:
                return k
            k+=1

# Optimal Solution
    # Goal: make O(N) searach -> O(logN)
    # Keyword:  "Find the minimum or maximum value to pass a test.">  Binary Search on Answer
    # Approach: Traverse the array with l, r pointer with while loop to compare mid value with target, remember "=" to ensure the loop still runs when the search range shrinks to a single element

class Solution:  
    def minEatingSpeed(self,piles:List[int],h:int):
        l,r = 1, max(piles) #max speed
        res = 0
        while l<=r:
            mid = (l+r)//2
            total_hours= 0
            for pile in piles:
                total_hours += (pile + mid -1) // mid
            if total_hours <= h: # we can search for less speed
                res = mid
                r = mid-1
            else:
                l = mid +1 
        return res
                
# Time Complexity: O(MlogN) ....  M is the total number of piles in the input array, N is the search range on the answer, 
# Space Complexity: O(1)... We didn't create extra variable or data structure

def test():
    sol = Solution()
    piles = [1,4,3,2]
    h = 9
    result = sol.minEatingSpeed(piles,h)
    print(f"Result:{result}")

if __name__ == "__main__":
    test()


