class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        # 定義 DFS，多帶一個參數：目前這條路上的 "最大值"
        def dfs(node, max_so_far):
            # 【動作 1：停】
            if not node:
                return 0
            
            # 【動作 1.5：判】
            # 判斷我自己是不是 Good Node
            res = 0
            if node.val >= max_so_far:
                res = 1
            
            # 更新要傳給子孫的 "最高紀錄"
            # 如果我比紀錄高，就用我的值當新門檻；否則維持原案
            new_max = max(max_so_far, node.val)
            
            # 【動作 2：叫】
            # 把新的門檻傳下去
            res += dfs(node.left, new_max)
            res += dfs(node.right, new_max)
            
            # 【動作 3：算】
            return res
        
        # 啟動：根節點的門檻就是它自己 (或是負無窮大也可以)
        return dfs(root, float('-inf'))