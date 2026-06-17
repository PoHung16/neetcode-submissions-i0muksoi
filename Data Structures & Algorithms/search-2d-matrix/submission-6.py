"""
 OOD: No
 Constraints: Yes
 input : List[List[int]],int
 output : boolean
"""
# Keyword : “Sorted Array " or "Sorted 2D matrix" or "Search in rotated array" -> Basic Binary Search
# Image :  Traverse the array with l, r pointer
# Tricks :  
    # Common Situation: 
        # A. The squeeze use "while l <= r” ensures the loop still runs when the search range shrinks to a single element.
        # B. We compare the mid value with target, if equal we find it, it target is smaller, we search left side, if target is larger, we search the right side
    # 2D Array Situation
        # row = mid // n , col = mid % n 



        # B-2. Identify the cliff (Rotated Array):  We compare the mid value with nums[r] , if mid value is greater, left side is normal slope
        # C. Shrink:  In normal slope side, we perform binary search
    # Find "minimum" in Rotated Sorted Array Situation: 
        # A. The squeeze use ""while l < r", the loop automatically stops when only one element being left. This will be mininum
        # B. Identify the cliff (Rotated Array):  We compare the mid value with nums[r] , if mid value is greater, left side is normal slope
        # C. Shrink: If left side is normal slope,  minimum will be on right side. Otherwise,  minimum will be on left side or itself  ps.[6,1,2]

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target:int)->bool:
        m, n = len(matrix), len(matrix[0])
        l, r = 0 , m*n-1
        while l<=r:
            mid = (l+r)//2
            row = mid // n
            col = mid % n
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False

def test():
    sol = Solution()
    matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
    target= 4
    result = sol.searchMatrix(matrix,target)
    print(f"Result:{result}")

if __name__ == "__main__":
    test()

# Time Complexity: O(logM*N) .... Since its divided by h times, 2^h = n, h = logN
# Space Complexity: O(1)... We didn't create extra variable or data structure       




