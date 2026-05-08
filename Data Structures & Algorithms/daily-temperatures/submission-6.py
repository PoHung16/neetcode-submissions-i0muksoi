"""
 OOD: No
 Constraints: No
 input : List[int]
 output : List[int]
"""
# Keyword : “Parentheses","Reverse Polish Notation" -> Basic Stack
# Image: Traverse the array
# 1.push new element into monotonic decreasing stack bc the smaller cannot save the current element but it could be saved by future element.
# 2.pop the index while stack  is not empty and greater element come save and record the gap

from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                prev_idx = stack.pop()
                gap = i - prev_idx
                res[prev_idx] = gap
            stack.append(i)
        return res

def test():
    sol = Solution()
    temperatures = [30,38,30,36,35,40,28]
    result = sol.dailyTemperatures(temperatures)
    print(f"Result:{result}")

if __name__ == "__main__":
    test()

# Time complexity: O(N) ... Traverse size N Array
# Space complexity:  O(N)....create size N Stack  & size N result






