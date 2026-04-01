class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #Step1:  初始化 answer 陣列  and 空stack
        #Answer陣列用來儲存每個index需要等多少天才有暖陽
        #Stack: 等待名單 - 用來紀錄每個index
        n = len(temperatures)
        ans = [0]*n
        stack = []
        #Step2:  For loop traverse temperatures with index
        for i, t in enumerate(temperatures):
            #Step2-1: Process elements using the stack under 2 condition  (While loop)
            #stack 有人在等
            #今天的溫度比等待名單temperatures[stack[-1]]的人熱 ,代表等到了
            while stack and t > temperatures[stack[-1]]:
                #Step2-2 :pop 等待名單的index & 填表
                stack_index = stack.pop() 
                ans[stack_index] = i -stack_index
            #Step2-3 : 把自己append「等待名單」 
            stack.append(i)
        #Step 3: 回傳結果
        return ans

        