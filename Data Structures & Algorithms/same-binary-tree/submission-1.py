class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #思路： 看到Binary Tree , 「不需要父節點的資訊，只需要子節點資訊」
        #題型：基本Bottom-Up DFS
        #Step1:  Edge case :走到底了
        if not p and not q:
            return True
        if not p or not q:
            return False
        #Step2:  慣老闆不想動沒有base case or偶爾動一下有base case 
        if p.val != q.val:
            return False
        #Step 3: 向手下要結果，回報給真正大老闆
        left = self.isSameTree(p.left,q.left)
        right = self.isSameTree(p.right,q.right)
      
        return left and right 


















        
        # 1. 兩個都空 -> 代表這條路比完了，沒問題 -> True
        if not p and not q:
            return True
        
        # 2. 一個空一個不空 -> 結構不一樣 -> False
        # (因為上面的 if 已經排除了 "兩個都空"，所以這裡只要有一個空就是不一樣)
        if not p or not q:
            return False
        
        # 3. 兩個都有值，但是數字不一樣 -> 數值不一樣 -> False
        if p.val != q.val:
            return False
            
        # 【動作 2 & 3：叫 & 算】(Call & Compute)
        # 既然我自己這層沒問題，那就信任小孩
        # 只有當 "左邊一樣" 且 "右邊一樣"，整棵樹才是一樣的
        return self.isSameTree(p.left, q.left) and \
               self.isSameTree(p.right, q.right)







               