"""
 OOD: No
 Constraints: Yes
 input : List[List[int]],int
 output : boolean
"""
# Keyword : “Sorted Array " or "Sorted 2D martix" -> Basic Binary Search
# Image : Traverse the array with l, r pointer, and we compare the mid value with target, if equal we find it, it target is smaller, we search left side, if target is larger, we search the right side
# Tricks :  
    # use “=”, "l <= r” ensures the loop still runs when the search range shrinks to a single element.
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target:int)->bool:
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m*n-1
        while l<=r :
            mid = (l+r) //2
            row = mid // n
            col = mid % n
            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                r = mid-1
            else:
                l = mid + 1
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




