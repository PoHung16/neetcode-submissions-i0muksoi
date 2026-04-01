class TimeMap:

    def __init__(self):
        # 我們用一個 Dictionary (Hash Map)
        # Key 是字串, Value 是一個 List，裡面存 [val, time]
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        # 如果 Key 不存在，先開一個空的 List
        if key not in self.store:
            self.store[key] = []

        # 把新的資料 Append 進去。
        # 重點：題目保證 timestamp 是 "strictly increasing" (嚴格遞增)
        # 這代表我們的 List 永遠是自動排序好的 (Sorted)，不需要自己 Sort！
        self.store[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        # Edge Case: 如果連這個人名(Key)都沒有，直接回傳空
        res = ""
        if key not in self.store:
            return res

        # 拿到這個 Key 對應的 List, [val, time]
        values = self.store[key]

        # --- BINARY SEARCH 模板開始 ---
        
        # Step 1: 初始化「範圍全開」
        L, R = 0, len(values) - 1
        # Step 2: 循環「手沒交叉就不停」
        while L <= R:
            mid = (L + R) // 2
            
            # 從 List 裡拿出 [數值, 時間]
            cur_val, cur_time = values[mid]
            
            if cur_time <= timestamp:
                # Step 3 (Valid): 這個時間點發生在目標時間「之前」或「當下」。
                # 這是潛在的答案！先記下來。
                res = cur_val
                
                # 策略：因為我們要找「最接近 (Most Recent)」的，
                # 所以要試著往「右邊」找找看有沒有更晚的時間點。
                L = mid + 1
            else:
                # Step 4 (Invalid): 這時間點發生在「未來」。
                # 太大了，滾吧！往左邊找過去的時間。
                R = mid - 1
                
        # --- BINARY SEARCH 模板結束 ---
        
        return res












