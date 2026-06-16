"""
 OOD: No
 Constraints: No
 input : List[int]
 output : List[int]
"""
# Keyword : “Next greater or smaller element" or "Blocking" Effect"-> monotonic stack
# Image: Traverse the array, 
# 1. while/if monotonic stack is being unblocked or saved, pop the index to calculate the day gaps.
# 2. Push new element into a monotonic increasing/decreasing stack 

from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i, value in enumerate(temperatures):
            while stack and value > temperatures[stack[-1]]:
                prev_idx = stack.pop()
                gap = i - prev_idx
                res[prev_idx] = gap
            stack.append(i)
        return res
# Time complexity: O(N) ... Traverse size N Array
# Space complexity:  O(N)....create size N Stack  & size N result array

def test():
    sol = Solution()
    temperatures = [30,38,30,36,35,40,28]
    result = sol.dailyTemperatures(temperatures)
    print(f"Result:{result}")

if __name__ == "__main__":
    test()






