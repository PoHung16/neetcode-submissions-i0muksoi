from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []  # 存放最終所有子集的結果列表
        
        # start: 當前可以從 nums 的哪個索引開始選數字
        # path: 當前正在構建的子集（路徑）
        def backtrack(start: int, path: List[int]):
            # 1. 紀錄結果：
            # 在子集問題中，決策樹的每一個節點都是一個合法子集
            # 使用 path[:] 是為了深拷貝當前的列表內容，避免後續修改影響到已存入 res 的結果
            res.append(path[:])
            
            # 2. 遍歷選擇：
            # 從 start 開始往後選，保證我們不會選到重複的組合（例如選了 [1,2] 就不會再選 [2,1]）
            for i in range(start, len(nums)):
                
                # --- 選 (Choose) ---
                # 將當前數字加入路徑
                path.append(nums[i])
                
                # --- 探 (Explore) ---
                # 遞迴進入下一層，start 傳入 i + 1，代表下一個數字必須從當前數字的後面選
                backtrack(i + 1, path)
                
                # --- 撤 (Backtrack) ---
                # 回溯：將最後加入的數字彈出，恢復現場，以便嘗試下一個數字
                path.pop()
        
        # 從索引 0 開始，初始路徑為空集
        backtrack(0, [])
        return res

        