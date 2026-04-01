class RandomizedSet:
    #思路：
    #記住我看過什麼：檢查字串某個元素是否出現過
    #OOD -> 每個function都要顧到init
    #題型：HashMap題型 +OOD題型

    def __init__(self):
        #Step 1:  Initiate a map, store the key-value pair
        self.numArray = [] # index : value
        self.hashMap = {} # value : index
    def insert(self, val: int) -> bool:
        if val in self.hashMap:
            return False
        #Step 2:  Iterate over hashMap
        #Add the element to the Map
        self.hashMap[val] = len(self.numArray) #最後一個位置
        self.numArray.append(val) #最後一個位置
        return True
    #1,2,3 -> # 1,3,3 -> 1,3
    def remove(self, val: int) -> bool:
        if val not in self.hashMap: # val = 2
            return False
        # 取得要刪除目標的索引，以及目前陣列的最後一個元素
        idx_to_remove = self.hashMap[val] # current_index =1
        lastElement = self.numArray[-1] #lastElement = 3
        #把最後一個元素搬到目標位置 (覆蓋掉要刪除的 val)
        self.numArray[idx_to_remove] = lastElement
        #更新最後一個元素在字典中的新索引
        self.hashMap[lastElement] = idx_to_remove
        self.numArray.pop()
        del self.hashMap[val] # 這是你原本漏掉的關鍵！

    def getRandom(self) -> int:
        return random.choice(self.numArray)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()