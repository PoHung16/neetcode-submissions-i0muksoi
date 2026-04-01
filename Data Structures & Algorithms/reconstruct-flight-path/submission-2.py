from collections import defaultdict
class Solution: 
    # 題型Keyword: "Reconstruct Flight Path” -> Advanced graph
    # 腦中圖像: Imagine you are pulling a string through a series of airports, each flight ticket means an edge. If you hit a dead end, that means thats the last airport. And you can backtrack to find the path. THen reverse it to get the answer
    # 動作記憶法 - 三個步驟 
    def findItinerary(self, tickets):
        # ps. Edge case
        if not tickets:
            return []
        # ps.Decide if its’ a matrix or adjacent list graph -> adjacent list graph 
        # Step 1: Build the Graph directed or undirected graph (Only for Adjacent graph) 
        res = []
        graph = defaultdict(list)
        # Step 1-1 sort the ticket in reverse : [Z,C,A]
        for a, b in sorted(tickets, reverse = True):
            graph[a].append(b)
        # Step 2: Exploring Phase - dfs (Adjacent graph Version)
        def dfs(i):
            # 2-a Base case: no base case
            # 2-b Every Layer： No MARK & MOVE (Since it only have one neighbor)
            while graph[i]:
                next_dest = graph[i].pop() # get the next station (the lexical smallest one)
                dfs(next_dest)
            # 2-c append the final destination to our result path
            res.append(i)

        # Step3 :Scanning Phase : Perform Dfs on single element  to find result
        dfs("JFK")

        # Step 4: Return Result -reverse
        return res[::-1]

# Time complexity: O(V+E) ...visited all nodes and its neighbor
# Space complexity:  O(V+E)....create size V directed graph but each vertex have e neighbor
def test():
    sol = Solution()
    result = sol.findItinerary([["HOU","JFK"],["SEA","JFK"],["JFK","SEA"],["JFK","HOU"]])
    print(f"Result: {result}")
test()


