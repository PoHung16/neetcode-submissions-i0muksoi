class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Step 1: 初始化
        l = 1
        r = max(piles)
        res = 0
        # Step 2: 循環
        while l <= r:
            # Step 3 :判斷 can_finish(mid)
            def can_finish(mid):
                total_time = 0
                for p in piles:
                    # 每一堆要吃幾次？ 天花板除法：(p + k - 1) // k
                    # 如果你想讓 p 在除法中「提早進位」，你只需要在 p 上加上一個 「差一點點就能湊滿一整份」 的數量
                    total_time += (p + mid -1) // mid
                if total_time <= h:
                    return True
                else:
                    return False
        
            # Step 4 : 移動
            mid = (l + r) //2
            if can_finish(mid):
                res = mid
                r = mid - 1
            else:
                l = mid +1
        return res
        
        
        
        
        
        
    

        






