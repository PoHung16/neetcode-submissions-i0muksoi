class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # 1. 樹的先決條件：邊的數量必須是 n - 1
        # 如果邊太多會有環，邊太少則不連通
        if len(edges) != n - 1:
            return False
        
        # 2. 建立鄰接表
        adj = {
            i : [] for i in range(n)
        }


        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        visited = set()

        # 3. 定義 DFS 模板，傳入目前節點和它的父節點
        def has_cycle(curr, prev):
            visited.add(curr)
            
            for neighbor in adj[curr]:
                # 如果鄰居是父節點，跳過（無向圖的正常回頭）
                if neighbor == prev:
                    continue
                
                # 如果鄰居已經造訪過，代表我們繞了一圈回來了 -> 有環！
                if neighbor in visited:
                    return True
                
                # 遞迴檢查鄰居，如果鄰居的子孫有環，也回傳 True
                if has_cycle(neighbor, curr):
                    return True
            
            return False

        # 4. 從節點 0 開始搜尋
        # 如果偵測到環，則不是樹
        if has_cycle(0, -1):
            return False
            
        # 5. 最後檢查連通性：是否所有點都走到了
        return len(visited) == n