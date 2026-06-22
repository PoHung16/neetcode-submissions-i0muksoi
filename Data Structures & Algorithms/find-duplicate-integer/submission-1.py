"""
 OOD: No
 Constraints: No
 input : ListNode
 output : ListNode
"""
"""
class ListNode:
    def __init__(self, val=0,next=None):
        self.val = val
        self.next = next
""" 
# Keywords: "LinkedList Cycle", "Find mid in LinkedList" or "Find the Duplicate Number in O(1) space complexity"-> Fast/Slow pointer
# Image : while fast and fast.next to traverse linkedlist to check cycle with 'slow', 'fast'. Return List head
# Tricks
    # Array to Linked List Cycle situation (Find Duplicate):
        # A. Step 1: Check if there's cycle
        # B. Step 2: find the entrance of the cycle (2 pointer move at the same speed) - one from the meet point, the other from the start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Step 1: Check if there's cycle
        fast = 0
        slow = 0
        while True:
            slow = nums[slow]          # 慢指针走一步: slow = slow.next
            fast = nums[nums[fast]]    # 快指针走两步: fast = fast.next.next
            if slow == fast:
                break
       
        # Step 2: find the entrance of the cycle (2 pointer move at the same spped) - one from the meet point, the other from the start
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow

# Time complexity: O(N) ... Traverse size N LinkedinList
# Space complexity:  O(1)....create constant variable

def test(): 
    nums = [1,2,3,2,2]
    sol = Solution()
    result= sol.findDuplicate(nums)
    print(f"Result:{result}")

if __name__ == "__main__":
    test()


 

