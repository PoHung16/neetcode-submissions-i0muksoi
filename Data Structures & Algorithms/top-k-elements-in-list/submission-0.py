class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        arr = []
        #count.items() 可以同時拿到key (element) 和 value (count)
        for num, cnt in count.items(): 
            arr.append([cnt, num])#append value(count), key(element) 
        arr.sort() #sort on value(count)

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res