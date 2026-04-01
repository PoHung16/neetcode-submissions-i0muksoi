import collections

class Solution: # <--- 加上這一行
    def findItinerary(self, tickets): # <--- 加上 self
        # Step 1: Build the Graph
        graph = collections.defaultdict(list)
        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)
        
        itinerary = []

        # Step 2: Exploring Phase (DFS)
        def dfs(curr):
            while graph[curr]:
                next_dest = graph[curr].pop()
                dfs(next_dest)
            itinerary.append(curr)

        # Step 3: Scanning Phase
        dfs("JFK")

        # Step 4: Return Result
        return itinerary[::-1]