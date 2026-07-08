"""
 OOD: No
 Constraints: No
 input : List[int]
 output : List[int]
"""
# Brute Force: 
    # Use two nested loops - outer loop selects a day , inner loop  - scans through all future days until it finds a  higher temperatur -> O(N^2)
class Solution:
    def dailyTemperatures(self,temperatures:List[int])->List[int]:
        result=[0]*len(temperatures)
        for i in range(len(temperatures)):
            for j in range(i+1,len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    result[i] = j-i
                    break # Found the next warmer day, stop searching
        return result


# Optimal Solution
    # Keyword : “Next greater or smaller element" or "Blocking" Effect"-> monotonic decreaing stack (棧底到棧頂越來越小)
    # Approach: Traverse the array to use monotonic stack to record waitlist index, 
        # while/if monotonic stack is being unblocked, pop out the index to calculate the day gaps and store into result array
    
from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
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






