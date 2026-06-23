"""
 OOD: No
 Constraints: No
 input : ListNode
 output : ListNode
"""
# Keywords: "LinkedList Cycle", "Find mid in LinkedList" or "Find the Duplicate Number in O(1) space complexity"-> Fast/Slow pointer
# Image : while fast and fast.next to traverse linkedlist to check cycle with 'slow', 'fast'. Return List head
# Tricks
    # Array to Linked List Cycle situation (Find Duplicate):
        # A. Step 1: Check if there's cycle
        # B. Step 2: find the entrance of the cycle (2 pointer move at the same speed) - one from the meet point, the other from the start

class ListNode:
    def __init__(self, val=0,next=None):
        self.val = val
        self.next = next

class Solution:
    def findDuplicate(self,nums:List[int]) -> int:
        # Step 1: Check if there's cycle
        fast = 0
        slow = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break
        
        # Step 2: find the entrance of the cycle (2 pointer move at the same speed) - one from the meet point, the other from the start
        slow2 = 0
        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
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


 

