class Solution:
    # 主函數：負責 "找" (Search)
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # 【動作 1：停】
        # 如果目標是空的，永遠視為成功 (視題目定義，通常 leetcode 不會有這情況但寫著保險)
        if not subRoot: return True
        # 如果大樹已經找光了還沒找到 -> 失敗
        if not root: return False
        
        # 【動作 1.5：判】(Check)
        # 立刻比對：現在這個位置，是不是就是我要找的那棵樹？
        # 呼叫小幫手 isSameTree
        if self.isSameTree(root, subRoot):
            return True

        # 【動作 2：叫】(Call)
        # 如果我這層不是，那就去 "左子樹找" 或者 "右子樹找"
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

            
        # 【動作 3：算】
        # 只要有一邊回傳 True，就是找到了
        return left or right
               

    # ------------------------------------------------
    # 小幫手函數：負責 "比" (Compare - 上一題的 Code)
    def isSameTree(self, p, q):
        if not p and not q: return True
        if not p or not q or p.val != q.val: return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)



