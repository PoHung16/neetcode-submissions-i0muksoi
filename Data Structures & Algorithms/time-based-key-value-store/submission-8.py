"""
 OOD: Yes
 Constraints: No
 input : constructor and method
 output : constructor and method
"""
# A.Clarify the goal : Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.
# B.Design the data structure : 
    # 1. HashMap : O(1) with insert/Delete/LookUp  -> HashMap
    # 2. Binary Search :  Search the closest value to a target value in sorted Array -> Basic binary serach
#C.Implement constructor and method
# Tricks:
    # if hashmap's key contains multiple value: use defaultdict(list) - or defaultdict(set) check duplicate
from collections import defaultdict
class TimeMap:
    def __init__(self):
        self.hashMap = defaultdict(list)
    def set(self, key:str, value:str, timestamp:int):
        self.hashMap[key].append((value,timestamp)) #{key : (value, timestamp)}
    def get(self, key:str, timestamp:int)-> str:
        if key not in self.hashMap:
            return ""
        values = self.hashMap[key] # [(value1, timestamp1), (value2, timestamp2)]
        l, r = 0, len(values)-1
        closetValue = ""
        while l<=r:
            mid = (l+r)//2
            mid_value, mid_time = values[mid]
            if mid_time == timestamp:
                return mid_value
            elif mid_time < timestamp:
                closetValue = mid_value
                l = mid + 1
            else:
                r = mid -1
        return closetValue


def test():
    timeMap = TimeMap()
    timeMap.set("alice", "happy", 1)
    print(f"get(alice, 1): {timeMap.get('alice', 1)}") # 預期輸出: "happy"
    print(f"get(alice, 2): {timeMap.get('alice', 2)}") # 預期輸出: "happy" (因為 1 是小於 2 的最大時間戳)
    timeMap.set("alice", "sad", 3)
    print(f"get(alice, 3): {timeMap.get('alice', 3)}") # 預期輸出: "sad"

if __name__ == "__main__":
    test()

# Time Complexity: 
    # get: O(logN)...perform binary Search
    # set: O(1) 
# Space Complexity: O(N)... create size N Map. total number of (Key, value) is N
