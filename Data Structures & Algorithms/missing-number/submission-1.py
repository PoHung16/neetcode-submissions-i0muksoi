class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 題型Keyword: "Missing Number"
        # 這題雖然有duplciate但因為強制space complexity 要O(1)所以不能用hashmap
        # 腦中圖像: “消消樂” -> 索引跟數字配對，剩下的就是缺的那一個。

        # Step 1: 先找到範圍最大的那個value，因為for loop沒包括最大的數字
        res = len(nums)
        # Step 2: Iterate the loop to process 消消樂
        for i in range(len(nums)):
            # 索引 i 跟 數字 num 互相消消樂. 把所有的索引先相加，再減去所有數字
            res += i
            res -= nums[i]            
        #Step 3 : Return result
        return res

        '''
        Time Complexity : O(N) -> traverse size N 陣列
        Space Complexity : O(1) -> 只創了一個變數 res
        '''