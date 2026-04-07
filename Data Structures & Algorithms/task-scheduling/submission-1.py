class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        # Keyword : minimum number -> Global Minimum/Maximum with sort
        # Image: Use the most frequent tasks to build the frame. The cooldown ($n$) is the gap between them. Think of the other tasks as filler bricks. You stuff them into the gaps to stay busy. If you run out of bricks, you have Idle spots. If you have too many, the building just gets taller.



        # Step 1: Frequency count arrat & Sort to find the max_frequency
        count = [0] * 26
        for task in tasks:
            count[ord(task) - ord('A')] += 1
        count.sort()
        max_f = count[25]
        # Step 2: Construct the Empty Frame for the max_frequency and fill it
        # A _ _ A _ _ A (max_f = 3, n = 2) -> 2 gaps of length 2
        idle_slots = (max_f - 1) * n
        for i in range(24, -1, -1): # We start from the 2nd most frequent task (index 24)
            idle_slots -= min(max_f - 1, count[i]) # # A task can't fill more than (max_f - 1) slots

        #Step 3 : Return result        
        # If idle_slots becomes negative, it means we have more tasks than gaps. # 這些任務太多了，它們光是互相穿插，就已經遠遠超過了 idle = n 的限制。
        return max(0, idle_slots) + len(tasks)



# Time : O(N)
    # Sort : O(26 log 26)-> O(1)
    # Traverse an array: O(N)
# Space: O(1)...create size 26 array


