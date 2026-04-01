class Solution:
    def partition(self, s: str) -> List[List[str]]:
        #Step 1: initialize the final result to store our subsets
        res, part = [], []
        #Step 2: define dfs function : def dfs(i)

        def dfs(i):
            #Step2-1: Base case : when to stop and what should we do
            if i >= len(s):
                res.append(part.copy())
                return
            #Step2-2: Decision Tree Start : include which one with條件
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    part.append(s[i : j + 1])
                    dfs(j + 1)
                    part.pop()
        #Step 3: call dfs function and return result
        dfs(0)
        return res

    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True