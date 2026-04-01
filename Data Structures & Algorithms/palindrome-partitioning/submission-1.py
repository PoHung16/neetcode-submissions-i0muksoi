class Solution:
    def partition(self, s: str) -> List[List[str]]:
        #Step 1: initialize the final result to store our subsets
        res = []
        #Step 2: define dfs function : def dfs(i)
        def dfs(i, subset):
            # Step2-1: Base case : when to stop and what should we do
            if i == len(s):
                res.append(subset.copy())
                return
            # Start with all different element, each time add one more, i is start, j is end
            for j in range(i, len(s)):
                #Step2-2: Constraints:  Constraints : decide if it is palidrome
                if self.isPali(s, i, j):
                    # #Step2-3:  Choices with Backtracking  : include  more other elements
                    subset.append(s[i : j + 1])
                    dfs(j + 1,subset)
                    subset.pop()
        #Step 3: call dfs function and return result
        dfs(0,[])
        return res

    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True