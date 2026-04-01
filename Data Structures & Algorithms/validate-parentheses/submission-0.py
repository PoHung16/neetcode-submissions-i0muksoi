class Solution:
    def isValid(self, s: str) -> bool:
        #思路：「最後一個開啟的括號，必須第一個被關閉- 」->LIFO
        #題型：一般stack 題型
        # Step 1: 建立對應表 (右找左) 和空stack記錄左括號
        closeToOpen = {")": "(", "}": "{", "]": "["}
        stack = []
        #Step 2: For Loop 遍歷字串中的每個字元
        for c in s:
            # Step 2-1:它是右括號嗎？
            if c in closeToOpen:
                # A.檢查 Stack 是否為空？或者 Stack 頂端是不是它要的伴？
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                #如果不匹配or不存在 → 回傳 False。
                else:
                    return False
            else:
                # 如果是左括號，直接入棧
                stack.append(c)
        
        # Step3 : 回傳結果
        return len(stack) == 0