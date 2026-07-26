"""
 OOD: No
 Constraints: No
 input : List[int]
 output : List[int]
"""
# result[i] is reflecting how many days next greater temperature show up
# Brute Force: 
    # Array - Use two nested loops to calculate the gap -> O(N^2)
class Solution:
    def dailyTemperatures(self,temperatures:List[int])->List[int]:
        res = [0]*len(temperatures)
        for i in range(len(temperatures)):
            for j in range(i+1,len(temperatures)):
                if temperatures[j] >temperatures[i]:
                    res[i] = j-i
                    break  # Found the next warmer day, stop searching
        return res

# result[i] is reflecting how many days next greater temperature show up
# Optimal Solution
    # Goal : O(N^2)->O(N)
    # Keyword : “Next greater or smaller element" or "Blocking" Effect"-> monotonic decreaing stack (棧底到棧頂越來越小)
    # Approach: 
        # 1.Use a Stack to track pending element index
        # 2.Traverse the array 
            # while stack and stack is being unblocked(find the next greater one), pop the stack, calculate the gap
from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # track pending element index
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






