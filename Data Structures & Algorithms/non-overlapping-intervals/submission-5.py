"""
 OOD: No
 Constraints: No
 input : List[List[int]]
 output : int
"""

# Optimal Solution
    # Keyword: “Return the Minimum number" -> Greedy Choice, we choice intervals that end ealier first to allow more interval coming , then we get the mininum number we need to remove
    # Approach:
        # Edge case
        # 1. Sort : Sort by END time (x[1])
        # 2. Track : Track the end time of last remaining interval & count
        # 3. Single Loop to traverse the interval:
            # if conflict : previous end> current start ,removed_count+=1
            # no conflict : update previous end
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]])->int:
        # edge case
        if not intervals:
            return 0
        # 1.Sort : Sort by END time (x[1])
        intervals.sort(key=lambda x:x[1])
        # 2.Track the end time of last remaining interval & count
        prev_end = intervals[0][1]
        removed_count = 0
        # 3.Single Loop to traverse the interval:
        for i in range(1,len(intervals)):
            # if conflict : previous end> current start ,removed_count+=1
            if prev_end > intervals[i][0]:
                removed_count+=1
            # no conflict : update previous end
            else:
                prev_end = intervals[i][1]
        return removed_count


# Time Complexity: O(N log N) 
    #- O(N log N) for sorting intervals by end time
    #- O(N) for single loop linear scan
    #- Total: O(N log N)
# Space Complexity: O(1)  

def test():
    sol = Solution()
    intervals = [[1,2],[2,4],[1,4]]
    result = sol.eraseOverlapIntervals(intervals)
    print(f"Result:{result}") # Expected output: 1 (remove [1,4])
if __name__ == "__main__":
    test()