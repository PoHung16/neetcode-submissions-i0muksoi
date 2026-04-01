class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #思路： 題目提到「連續子陣列」或「連續子字串」 - 陣列中只有正數
        #題型：Sliding Window 題型
        #Constraints: O(N)內解完，不能排序- >無法使用Sliding Window,因為排完序至少要O(NlogN)
        #題型：HashSet題型
        # Step 1: 把所有數字丟進 Set 裡
        numSet = set(nums)
        longest = 0
        # Step 2: Iterate over array
        for n in numSet:
            #Step2-1: if n-1 不在 set 裡，代表 n 是這段連續數字的老大.從起點開始往後數
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                # Step 2-3: 更新最大長度
                longest = max(length, longest)
        #Step 3: 回傳結果   
        return longest