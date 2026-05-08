"""
 OOD: No
 Constraints: No
 input : List[int]
 output : List[int]
"""
# Keyword : “Next greater or smaller element" -> monotonic stack
# Image: Traverse the array
# 1.push new element into monotonic decreasing stack bc the smaller cannot save the current element but it could be saved by future element.
# 2.pop the index while stack  is not empty and greater element come save and record the gap


class Solution:
    def carFleet(self,target: int, position: list[int], speed: list[int]) -> int:
        # Pair position with speed and sort by position descending 將位置與速度配對，並從距離終點「最近」的車開始遍歷
        cars = sorted(zip(position, speed), reverse=True)
        
        # Monotonic Stack: 用來存放每個車隊領頭車的到達時間
        # Logic: If a car behind is faster, it will be "saved" (blocked) by the fleet ahead.
        times = []
        for p, s in cars:
            arrival_time = (target - p) / s # Calculate the time needed to reach the destination
            times.append(arrival_time) # Step: Push new element into the stack
            
            # If the current car (behind) arrives EARLIER or EQUAL to the car ahead,
            # it means they collide and form a single fleet.
            # if len(times) >= 2 為了確保 Stack（疊棧）裡面至少有兩台車的時間，我們才能進行「前後車比較」。
            # times[-1] <= times[-2]後面的車小於前面的車
            if len(times) >= 2 and times[-1] <= times[-2]:
                times.pop() ## Pop the current car's time because it can't move faster than the leader
                
        return len(times) ## The number of elements remaining in the stack represents the number of unique fleets

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
# Space complexity:  O(N)....create size N Stack  & size N result array


            