# A. Clarify the goal: keep track of the 10 most recent tweets +post tweets + follow/unfollow each other
# B. Decide the data strucure
        # 1. follow/unfollow each other (我不重複追蹤同一個人,且我需要快速增加follow,unfollow）-> defaultdict(set)
        # 2. tweets (推文必須知道是「誰」發的，而且要能知道「先後順序」, 把新推文一直往後加（Append）) -> defaultdict(list)
            # 我們需要一個 全域計數器 (self.timer)-> self.timer = 0
        # 3. 10 most recent tweets(最小) : max_heap, 合併自己和所有追蹤者的推文，取最新的 10 條
# C. Implement constructor and method
# Keyword : Top K elements  -> Min Heap
# Image :  Imagine a smart funnel that only holds K spots, and the weakest/biggest ones get kicked out the top, where new elements "bubble" into place
# 3-Step Flow
# Step 1:  Initialize Max-Heap/Min-Heap simulation
# Step 2:  Traverse the array to perform heap operation
# Step 3:  return the result
import heapq
from collections import defaultdict

class Twitter:
    def __init__(self):
        self.following = defaultdict(set) # userId -> {followeeId}
        self.timer = 0
        self.tweets = defaultdict(list)   # userId -> [(time, tweetId)]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timer -= 1 # 負數模擬 Max-Heap，越小代表越新
        self.tweets[userId].append((self.timer, tweetId))

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        maxheap = []
        # 獲取所有相關用戶 (自己 + 追蹤的人)
        self.following[userId].add(userId)
        # 把追蹤者tweet都存到heap
        for followeeId in self.following[userId]:
            if followeeId in self.tweets:
                index = len(self.tweets[followeeId]) - 1
                time, tweetId = self.tweets[followeeId][index]
                heapq.heappush(maxheap, (time, tweetId, followeeId, index - 1))

        while maxheap and len(res) < 10:
            time, tweetId, followeeId, index = heapq.heappop(maxheap)
            res.append(tweetId)
            if index >= 0:
                time, tweetId = self.tweets[followeeId][index]
                heapq.heappush(maxheap, (time, tweetId, followeeId, index - 1))
        return res

#Time:
    #postTweet: O(1) ..append
    #follow / unfollow: O(1)...set insert/delete
    #getNewsFeed: O(K + log K)
        # Build Heap: 我們把 K 個追蹤者tweet都存到heap -> O(KlogK)
        # 提取 Top 10: 我們從 Heap 彈出一個元素並補入一個新元素: O(logK) *10

#Space: O(T+R)
    # build a size T hashmap : tweets ..... T is total tweets 
    # build a size R set : following..... R is the total following
    # getNewsFeed 執行時，build size K Heap 








