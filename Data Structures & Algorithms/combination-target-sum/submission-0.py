from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        # 排序可以讓我們在後續進行「剪枝」，提高效率
        candidates.sort()
        
        # remain: 還剩下多少額度要湊齊
        # path: 當前已經選入籃子的數字
        def backtrack(remain: int, start, path):
            # 第一部分
            # 紀錄結果 with 淺拷貝
            # --- 終止條件 ---
            if remain == 0:
                res.append(path[:]) # 找到一組正確答案，拍照記錄
                return
            
            # --- 遍歷選擇 ---
            for i in range(start, len(candidates)):
                # --- 剪枝 (Pruning) ---
                # 如果目前的數字已經超過剩下的額度，後面的數字更大，不用再試了
                if candidates[i] > remain:
                    break
                
                # --- 選 (Choose) ---
                path.append(candidates[i])
                
                # --- 探 (Explore) ---
                # 注意！這裡傳入 i 而不是 i + 1，表示下一層還能選當前的數字
                backtrack(remain - candidates[i], i, path)
                
                # --- 撤 (Backtrack) ---
                path.pop()
        
        backtrack(target, 0, [])
        return res