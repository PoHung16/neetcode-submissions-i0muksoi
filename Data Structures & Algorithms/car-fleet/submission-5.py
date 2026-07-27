"""
 OOD: No
 Constraints: No
 input : int, List[int], List[int]
 output : int
"""
# we need number of car fleet
# Brute force/ Optimal Solution:
    # Keyword : Array problem without keyword
    # Approach: 
        # 1. sort cars by zip(position,speed) by reverse
        # 2. calcuate the times for each car as list
        # 3. Use loop to simulate which cars catch up to earlier fleets & record fleet count and captain_arrive_time

class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = sorted(zip(position,speed), reverse=True)
        times = [(target-position)/speed for position, speed in cars]
        fleet_count = 0
        captain_arrive_time = 0
        for time in times:
            if time > captain_arrive_time: # means that it can not catch up the leader
                fleet_count+=1 # fleet count increment by 1
                captain_arrive_time = time # we need to update new captain arrive time
        return fleet_count
# Time complexity: O(N log N) ... sorted array
# Space complexity: O(N) ...create size N - times list

def test():
    sol = Solution()
    target = 10
    position = [1,4]
    speed = [3,2]
    result = sol.carFleet(target,position,speed)
    print(f"Result:{result}")

if __name__ == "__main__":
    test()




            