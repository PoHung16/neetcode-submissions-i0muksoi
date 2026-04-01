class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #思路： 看到「找下一個更大/更小」 (Next Greater / Smaller) 且需要計算「距離」時
        #題型：monotonic 題型
        #腦內圖像：腦內圖像：想像一排人在冷颼颼的候車室 (Stack) 坐著並領著號碼牌(index). 只要新來的溫度比我熱，從候車室踢掉乘客stack.pop(). 然後document 他坐了多久
        
        #Step1:  初始化 ans陣列計算各索引的距離  and  empty stack
        n = len(temperatures)
        ans = [0] * n
        stack = [] #guest room

        #Step2 : traverse all array with enumerate: 
        for i, t in enumerate(temperatures):
            #Step 2-1 Stack有人在等且新來的溫度> stack 頂端的溫度。踢掉那個guest -stack.pop()並計算距離
            while stack and t > temperatures[stack[-1]]:
                stack_idx = stack.pop()
                ans[stack_idx] = i -stack_idx
            #Step 2-2: 把新來的index放入候車室(stack.append(I))
            stack.append(i)
        #Step 3: 回傳結果

        return ans
        '''
        Time : O(N) … We traverse all string, N character
        Space: O(N) .. create a size N stack
        '''

