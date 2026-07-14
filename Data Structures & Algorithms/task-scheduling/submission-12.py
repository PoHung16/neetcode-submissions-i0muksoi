"""
 OOD: No
 Constraints: No
 input : List[String], int
 output : int
"""
# Brute Force: 
    # We simulate the CPU cycles step-by-step by greedily executing the most frequent task from a max heap and tracking cooldown times using a queue.
    # Time Complexity:
        # O(Total Cycles =tasks + all idle slots )
        # heapify: O(K)...k tasks, k is 26 at most -> O(26)

from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks) # Count frequencies of each task
        maxheap = [-cnt for cnt in counts.values()]
        heapq.heapify(maxheap)
        cooldown_queue = deque() # Queue to track tasks in cooldown:   pairs of (remaining_count, available_time)
        time = 0
        while maxheap or cooldown_queue:
            time += 1
            # If there's a task available, process it
            if maxheap:
                # Pop the most frequent task (convert back to positive)
                cnt = -heapq.heappop(maxheap)-1
                # If it still needs to be executed more, add to cooldown queue
                if cnt > 0:
                    cooldown_queue.append((cnt,time+n))
            # Check if the task at the front of the cooldown queue is ready to run again
            if cooldown_queue and cooldown_queue[0][1] == time:
                ready_task_cnt, _ = cooldown_queue.popleft()
                heapq.heappush(maxheap,-ready_task_cnt)
        return time

# Optimal Solution
  # Goal: O(T)-> O(N)
  # Keyword:  Rearrange items to maximize/minimize distance -> Greedy
  # Approach : We calculate the execution grid based on the most frequent task's cooling blocks and count trailing tasks to mathematically determine total time without running a loop.

from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 1. Greedily select the most frequent task
        counts = Counter(tasks)
        frequencies = list(counts.values())
        max_freq = max(frequencies)
        # 2. Count how many tasks share this maximum frequency
        max_freq_count = frequencies.count(max_freq) # (e.g., if A and B both appear 3 times, max_freq_count is 2)

        # 3.Calculate the minimum slots required based on the most frequent task
        # Formula: (max_freq - 1) * (n + 1) + max_freq_count
        # (max_freq - 1) is the number of full chunks/intervals created.
        # (n + 1) is the length of each intervals (1 task execution + n cooldown slots).
        # max_freq_count represents the trailing tasks executing at the very end.最後一個 A 後面不需要再冷卻了

        ans = (max_freq - 1) * (n + 1) + max_freq_count

        #  If the number of tasks is greater than our calculated minimum slots
        return max(ans, len(tasks))

       
# Time Complexity: O(N)
    # Traverse all tasks to count frequencies O(N)
    # Finding max frequencies takes O(26) = O(1) time.
# Space Complexity: O(1)
    # The hash map handles at most 26 uppercase English characters.

        
def test():
    sol = Solution()
    tasks = ["A","A","A","B","C"]
    n = 3
    result = sol.leastInterval(tasks,n)
    print(f"Result: {result}")
if __name__ == "__main__":
    test()
    
    
       
