class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #Step 1: 基本檢查&邊界條件 ：樹的先決條件：邊的數量必須是 n - 1
        # 如果邊太多會有環，邊太少則不連通
        if len(edges) != n-1:
            return False
        #Step 2: 初始化鄰接表和點名冊
        #建立adjacent List,記錄每個neighbor關係
        adj = {
            i : [] for i in range(n)
        }
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        #visited = set()，確保每個節點只被處理一次    
        visited = set()
        # Step 3: 定義 DFS 模板檢查有沒有環，處理三件事with三決策 - curr , prev
        def has_cycle(curr, prev):
            visited.add(curr)
            for neighbor in adj[curr]:
                #3-A 決策 A：如果鄰居是帶我過來的「爸爸」，這是雙向圖的正常回頭， continue跳過
                if neighbor == prev:
                    continue
                #3-B 決策 B：如果鄰居已經在點名冊裡了，而且他不是我爸爸, -> 抓到環了！
                if neighbor in visited:
                    return True
                #3-c # 決策 C：鄰居還沒去過，繼續往深處探險,# 如果深處發現了環，就一路把 True 傳回最上層
                if has_cycle(neighbor, curr):
                    return True
            return False
        #Step 4從節點 0 開始搜尋,如果偵測到環，則不是樹

        if has_cycle(0,-1):
            return False

        return len(visited) ==n












