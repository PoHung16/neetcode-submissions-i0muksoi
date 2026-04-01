from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        # 排 (Sort)：去重的先決條件
        candidates.sort()
        
        def backtrack(remain, start, path):
            # 第一部分
            # 紀錄結果 with 淺拷貝
            if remain == 0:
                res.append(path[:])
                return
            
            # 遍歷選擇
            for i in range(start, len(candidates)):
                # 剪 (Pruning)：同層去重
                # 如果 i > start，代表這不是這一層的第一個數字
                # 如果 candidates[i] == candidates[i-1]，代表這個數字剛才已經試過「當頭」了
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                # 超過目標值直接停止（因為數組已排序）
                if candidates[i] > remain:
                    break
                
                # 選 (Choose)
                path.append(candidates[i])
                
                # 探 (Explore)
                # 傳入 i + 1，保證每個元素只用一次
                backtrack(remain - candidates[i], i + 1, path)
                
                # 撤 (Backtrack)
                path.pop()
        
        backtrack(target, 0, [])
        return res