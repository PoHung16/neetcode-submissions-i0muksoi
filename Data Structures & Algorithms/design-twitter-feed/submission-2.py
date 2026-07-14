"""
 OOD: Yes
 Constraints: No
 input : constructor/method
 output : constructor/method
"""
# A. Clarify the goal:  keep track of the 10 most recent tweets + allows users to post tweets + follow/unfollow each other
# B. Decide the data strucure
    # Keyword: Bottom K elements  -> Max Heap
    # Approach :Traverse an array and  build a heap that only holds K spots, then kick out the smallest one on the top,  where new elements "bubble" into place
    # Keyword: O(1) with insert/Delete/LookUp-> HashMap
    # Image:  Imagine an instant-lookup Map Traverse an array to check if a Key or Value exists before , then perform following actions
    # Tricks: if hashmap's key contains multiple value: use defaultdict(list) - or defaultdict(set) check duplicate
# C. Implement constructor and method

import heapq
from collections import defaultdict
class Twitter:
    def __init__(self):
        self.tweets = defaultdict(list) # userId -> [(time, tweetId)]
        self.following = defaultdict(set) #userId -> {followeeId}
        self.time = 0
    def postTweet(self, userId:int, tweetId:int)->None:
        self.time+=1
        self.tweets[userId].append((self.time,tweetId))
    def follow(self, followerId: int, followeeId:int)->None:
        self.following[followerId].add(followeeId)
    def unfollow(self, followerId: int, followeeId:int)->None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
    def getNewsFeed(self,userId:int) -> List[int]:
        maxheap = []
        self.following[userId].add(userId) # add your own feed
        # 把每個follow人的最新動態先放到heap
        for followeeId in self.following[userId]:
            if followeeId in self.tweets:
                index = len(self.tweets[followeeId]) - 1 # latest index
                time, tweetId = self.tweets[followeeId][index] #  userId -> [(time1, tweetId1), (time2, tweetId2)]
                heapq.heappush(maxheap, (-time, tweetId, followeeId, index-1))
        res = []
        while maxheap and len(res) < 10:
            neg_time, tweetId, followeeId, next_index = heapq.heappop(maxheap)
            res.append(tweetId)
            # 如果該用戶還有更舊的推文，把下一則推入 Heap 中遞補, 可能可以取代另外一個followID最新的文，因為另外一個用戶第二新的文可能更新
            if next_index >= 0:
                time, t_id = self.tweets[followeeId][next_index]
                heapq.heappush(maxheap, (-time, t_id, followeeId, next_index - 1))
                
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








