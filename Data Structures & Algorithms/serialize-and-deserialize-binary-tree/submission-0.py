class Codec:
    # 思路：看到Binary Tree , 「不需要父節點的資訊，不用子節點資訊」 ，但此題需要一個global variable來記錄serialize string
    # 題型： 基本Top-Down DFS  ->Top-Down DFS with helper function
    # 腦內圖像：冒險者一路往下衝 
    def serialize(self, root)->str:
        #Step1:  定義global variable
        res = []
        #Step2:  定義dfs(node)
        def dfs(node):
            #Step2-1: Edge case +base case:  走到底了，冒險結束+每一層要做的事 build the root
            #Step 2-2:更新gloval variable
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            #Step2-3 :繼續往左、往右衝
            dfs(node.left)
            dfs(node.right)
        #Step 3: Call dfs +回傳結果 
        dfs(root)
        return ",".join(res) # to join list of string to a single string  -> 變成 "1,2,N,N,3,4,N,N,5,N,N"

    # 思路：看到Binary Tree , 「需要父節點的資訊，不用子節點資訊」
    # 題型： Top-Down DFS with helper function
    # 腦內圖像- Searh in BST(需要父節點idx資訊)： 冒險者按順序點名，包包裡裝著一個計數器 idx。每點到一個人，idxe 就加 1
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",") # to split a single string to  list of string
        #Step1:  定義global variable
        idx = 0
        #Step2:  定義dfs():不能有其他參數,因為children node還要傳給parent node
        def dfs():
            nonlocal idx
            val = vals[idx]
            #Step 2-2:更新gloval variable
            idx += 1
            #Step2-1: Edge case +base case:  走到底了 val = "N"，冒險結束+每一層要做的事 (建立root node)
            if val == "N":
                return None
            node = TreeNode(int(val))
            #因為要真的build a node, 所以要return node
            node.left = dfs()
            node.right = dfs()
            return node
        #Step 3: Call dfs +回傳結果
        return dfs()
        '''
        Time : O(N) …  Traverse N nodes in a binary tree
        Space: O(h) …The memory that store h recursive call occupies on the call stack, bc it will only execute one side left or right first.
        O(N)...Skewed Tree
        O(logn) … balanced tree
        '''