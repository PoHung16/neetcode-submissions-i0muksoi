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
# Keywords: "LinkedList Cycle", "Find mid in LinkedList"-> Fast/Slow pointer
# Image : while fast and fast.next to traverse linkedlist to check cycle with 'slow', 'fast'. Return List head
# Tricks
    # Array to Linked List Cycle situation (Find Duplicate):
        # A. Array as Pointer: Treat index as nodes and 'nums[i]' as the 'next' pointer.
        # B. Phase 1 (Meet): Move 'slow' 1 step and 'fast' 2 steps until they collide inside the cycle.
        # C. Phase 2 (Find Entrance): Reset 'slow' to start. Move both 1 step at a time; they will meet at the duplicate number.
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Step 1: 寻找快慢指针的相遇点（证明有环）
        slow = 0
        fast = 0
        
        while True:
            slow = nums[slow]          # 慢指针走一步: slow = slow.next
            fast = nums[nums[fast]]    # 快指针走两步: fast = fast.next.next
            if slow == fast:
                break
        
        # Step 2: 寻找环的入口（即重复的数字）
        # 让 slow 回到起点，fast 留在原地，两人同时每步走一下
        # slow 留在原地，新开一个 slow2 从数组起点出发
        slow2 = 0
        while True:
            slow = nums[slow]          # 相遇点的指针走一步
            slow2 = nums[slow2]        # 起点的指针走一步
            if slow == slow2:          # 再次撞车
                return slow            # 撞车点就是重复的数字
# Time complexity: O(N) ... Traverse size N LinkedinList
# Space complexity:  O(1)....create constant variable

def test(): 
   #2. run solution
    nums = [1,2,3,2,2]
    sol = Solution()
    result = sol.findDuplicate(nums)
    #3. prin it out
    print(f"Result: {result}")


if __name__ == "__main__":
    test()

 

