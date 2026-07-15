"""
 OOD: No
 Constraints: No
 input : TreeNode,int
 output : int
"""

# Optimal Solution
    # Keyword: BST problem - "K-th smallest/largest" OR "Sorted order output" OR "Successor/Predecessor" -> In-order DFS
    # Approach: base case -> delegate to left ->current node work -> delegate to right child
    # Tricks: 
        #   1. 用 In-order DFS 來保證走出來的數值是「從小到大排好序」的。
        #   2. 用外部變數 (nonlocal/global) 當作「共享筆記本」，這樣每次遞迴回頭點名時，大家才能共用同一個計數器。
class TreeNode:    
    def __init__(self, val=0 , left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Step 1: Initialize status variables to track result and count
        res = None
        count = k
        # Step 2: Define helper function to pass down state and prune search
        def dfs(node: TreeNode):
            nonlocal res, count
            
            # Step 2-1: Base Case & Short-circuit (If answer found, stop search)
            if not node or res is not None:
                return
            
            # Step 2-2: Delegate to left child first (Go to smaller values)
            dfs(node.left)

            # Step 2-3: Current Node Work (Check if this is the k-th smallest)
            count -= 1
            if count == 0:
                res = node.val
                return # Stop deeper recursion on this path
                
            # Step 2-4: Delegate to right child (Go to larger values)
            dfs(node.right)

        
        dfs(root)
        return res
# Time complexity: O(N) ...  Traverse N nodes in a binary tree,
# Space complexity:  O(h)....The memory that store h recursive call
    # O(N) ...Skewed Tree
    # O(logn) ... balanced tree  
def test():
    sol = Solution()
    
    # Constructing BST:
    root = TreeNode(5)
    root.left = TreeNode(3, TreeNode(1), TreeNode(4))
    root.right = TreeNode(8)
    
    # 測試案例 1: 找第 3 小的元素 (排序順序: 1, 3, 4, 5, 8 -> 第三個是 4)
    result1 = sol.kthSmallest(root, 3)
    print(f"Result 1 (3rd smallest): {result1}")  # 預期輸出: 4
    assert result1 == 4
    

if __name__ == "__main__":
    test()

        
