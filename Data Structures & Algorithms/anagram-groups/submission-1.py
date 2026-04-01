class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #思路： 分類/計數：把特徵相同的東西放在一起（如：Group Anagrams, Valid Sudoku）。
        #題型：字母/數字計數器題型
        #Step 1:  Initiate a defaultdict(list) map
        #當你存取一個不存在的 Key 時，它不會報錯（KeyError），而是自動幫你建立一個空的 list
        res = defaultdict(list)
        #Step 2:  Iterate over array
        for s in strs: # s為其中一個名詞 ex:"act"
            #Step2-1: 需要計算字母 - 字母計數器trick 
            #初始化陣列：count[0] *26
            #ASCII code填表：count[ord(c) - ord('a')] += 1
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1

            # Step 2-2: Add the element to the Map using append if the value is list
            # 注意：在 Python 中 list 是可變的 (mutable)，不能當 Key，
            # 必須轉成不可變的 tuple 才能存入字典。
            
            res[tuple(count)].append(s)
        # Step3: Return Result
        return list(res.values())
