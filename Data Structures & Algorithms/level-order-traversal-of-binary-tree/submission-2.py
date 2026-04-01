# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #思路： 看到Binary Tree , "Level Order" 或 "層級"
        #題型：BFS題型
        #腦內圖像: 自助餐排隊 (The Buffet Line) 服務生一次只放「這一批人」進去夾菜。這一批人夾完，換他們的「小孩」進來排隊。
        #Step 1:  Edge case 
        if not root:
            return []
        #Step 2 : Enqueue : 先把 Root 丟進去 Queue。
        queue = deque([root])
        res = []
        #Step 3 : Lock current level Size: while queue: level_size = len(queue) current_level = []
        while queue:
            current_level_size = len(queue)
            current_level = []
            #Step 4 : Scan
            for i in range(current_level_size):
                node = queue.popleft()
                current_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(current_level)
        return res

        '''
        Time : O(N) …  Traverse N nodes in a binary tree,
        Space: O(N) .... create size N queue
        '''



