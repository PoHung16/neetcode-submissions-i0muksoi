class TimeMap:
    #思路：
    #記住我看過什麼：檢查字串某個元素是否出現過
    #題目提到「Find/ Search in Sorted array」or「Logarithmic time - O(logn)」
    #題型：HashMap題型 + 一般Binary Search 題型
    def __init__(self):
        #Step 1:  Initiate a map, store the key-value pair
        self.hashMap = {}
    def set(self, key: str, value: str, timestamp: int) -> None:
        #Step 2:  Iterate over hashMap
        if key not in self.hashMap:
            self.hashMap[key] = []
        #Step2-2: Add the element to the Map
        self.hashMap[key].append([value,timestamp])

        #"foo" : ["bar", 1]
    def get(self, key: str, timestamp: int) -> str:
        #Step 1: 初始化左右指針 和 res
        res = ""
        values = self.hashMap.get(key,[]) #if no values, return []
        l = 0
        r = len(values) -1
        #Step 2: 循環 while L <= R「手沒交叉就不停」
        while l<=r:
            #Step 2-1: 計算 mid 並更新結果
            mid = (l+r) //2
            #Step 2-2: nums[mid] == target直接回傳
            if values[mid][1] == timestamp:
                res = values[mid][0]
                break
            if values[mid][1] < timestamp:
                res = values[mid][0]
                l = mid + 1
            else:
                #題目說一定要timestamp_prev,所以>timstamp, res不用更新
                r = mid -1
        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)