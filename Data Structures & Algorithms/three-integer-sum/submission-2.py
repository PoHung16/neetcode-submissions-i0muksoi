class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #思路： 資料已經排序 - 找對應的「一對」或「一組」數字 
        #題型：  Opposite pointer 題型
        #腦內圖像：固定一個數字先，再去用Two pointer 解Two Sum。有2個地方要避免重複的
        nums.sort()
        res = []
        for i, a in enumerate(nums):
            if i>0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum < 0:
                    l +=1
                elif threeSum >0:
                    r-=1
                else:
                    res.append([a,nums[l],nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l <r:
                        l+=1
        return res


  