"""
 OOD: No
 Constraints: No
 input : int, List[int],int
 output : int
"""
# Keyword : “Next greater or smaller element" or "Blocking" Effect"-> monotonic stack
# Image: Traverse the array, 
# 1. while/if monotonic stack is being unblocked or saved, means we finnd our result, pop the index to calculate the day gaps.
# 2. Push new element into a monotonic decreasing stack 
# Tricks:
    # 1. We need to zip position and speed together and sort in reverse bc the front car will block the back car
    # 2. Monotomic stack will save the arrival time period
class Solution:
    def carFleet(self,target: int, position: list[int], speed: list[int]) -> int:
        cars = sorted(zip(position,speed),reverse = True)
        times = []
        for p, s in cars:
            arrival_time = (target-p)/s
            times.append(arrival_time)
             # 判斷合併（核心邏輯）：後車(times[-1])」的時間小於等於「前車(times[-2])」
            if len(times) >= 2 and times[-1] <= times[-2]:
                times.pop()
        return len(times) #  ## The number of elements remaining in the stack represents the number of car fleets

def test():
    sol = Solution()
    target = 10
    position = [1,4]
    speed = [3,2]
    result = sol.carFleet(target,position,speed)
    print(f"Result:{result}")

if __name__ == "__main__":
    test()

# Time complexity: O(nlogn) 
    # O(nlogn) due to the sorting step.
    # Traverse Array is O(N)
# Space complexity:  O(N)....create size N Stack 


            