class TimeMap:
    def __init__(self):
        self.hashMap = {}
    def set(self, key: str, value:str, timestamp:int):
        if key not in self.hashMap:
            self.hashMap[key] = []
        self.hashMap[key].append([value,timestamp])
        ##"foo" : ["bar", 1]
    def get(self,key:str, timestamp:int):
        res = ""
        values = self.hashMap.get(key,[])
        l = 0
        r = len(values) -1
        while l<=r:
            mid = (l+r)//2
            if values[mid][1] == timestamp:
                res = values[mid][0]
                return res
            if values[mid][1] < timestamp:
                res = values[mid][0]
                l = mid + 1
            else:
                r = mid -1
        return res





        return res