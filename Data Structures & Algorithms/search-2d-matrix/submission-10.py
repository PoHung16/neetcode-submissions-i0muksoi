"""
 OOD: No
 Constraints: Yes
 input : List[List[int]],int
 output : boolean
"""
# Brute Force: 
    # Traverse the matrix to check every element to see if there's match -> O(M*N)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target:int) -> bool:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == target:
                    return True
        return False

# Optimal Solution
    # Goal: make O(N) searach -> O(logN)
    # Keyword:  "LogN complexity" or “Sorted Array " or "Sorted 2D matrix" or "Search in rotated array" -> Basic Binary Search
    # Approach: Traverse the array with l, r pointer with while loop to compare mid value with target, remember "=" to ensure the loop still runs when the search range shrinks to a single element
    # Tricks :  
        # 2D Array Situation: row = mid // n , col = mid % n 

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target:int)->bool:
        m, n = len(matrix), len(matrix[0])
        l,r = 0 , m*n-1
        while l <= r:
            mid = (l+r)//2
            row =  mid // n
            col =  mid % n
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] <= target:
                l = mid +1
            else:
                r = mid -1
        return False
# Time Complexity: O(logM*N) .... Since its divided by h times, 2^h = n, h = logN
# Space Complexity: O(1)... We didn't create extra variable or data structure       


def test():
    sol = Solution()
    matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
    target= 4
    result = sol.searchMatrix(matrix,target)
    print(f"Result:{result}")

if __name__ == "__main__":
    test()




