class Solution:
    def leastInterval(self,tasks: list[str], n:int) -> int:
        # Keyword : minimum number  -> Greedy with sort/ hashmap
            # Greedy is basically making the local optimal solution and hoping it leads to the global optimal solution
        # Image: 
            # Use the most frequent tasks to build the frame. The cooldown N is the gap between them. You need to fill the gap with other tasks
            #  If you run out of bricks, you have Idle spots.
            #  If you have too many, the building just gets taller.
        # Workflow - 3 Steps
            # Step 1: Get the max_frequency Task  as the frame
            # Step 2: Construct the Empty Frame for the max_frequency and fill it
            # Step 3 : Return result     
        # Tricks:
            #  If you need to find the max_frequency of a character, you must create a count array with 26 alphabet and then sort , and get the last element
        count = [0] * 26
        for task in tasks:
            count[ord(task)-ord("A")] += 1
        count.sort()
        max_freq = count[25]
        idle_slots = (max_freq-1) * n
        # A _ _ A _ _ A (max_f = 3, n = 2) -> 2 gaps of length 2
        # A task can't fill more than (max_f - 1) slots, since the task distance will <n 
        for i in range(24,-1,-1):
            idle_slots -= min(max_freq-1 ,count[i])

        # If idle_slots becomes negative, it means we have more tasks than gaps. 
        return len(tasks) + max(idle_slots,0)


# Time Complexity : O(N)
    # Traverse an array: O(N) 
    # Sort : O(26 log 26)-> O(1)
    # O(N) > O(1)
# Space: O(1)...create size 26 array


def test():
    sol = Solution()
    tasks = ["A","A","A","B","C"]
    n = 3
    result = sol.leastInterval(tasks,n)
    print(f"Result: {result}")
if __name__ == "__main__":
    test()
    
