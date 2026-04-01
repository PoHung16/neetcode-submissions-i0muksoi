class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Step 1:  Initiate a map, store the key-value pair
        #當你存取一個不存在的 Key 時，它不會報錯（KeyError），而是自動幫你建立一個空的 list
        res = defaultdict(list)
        #Step 2:  Iterate over array
        # s為其中一個名詞 ex:"act"
        for s in strs:
            # Step 2-1: build the key
            # 建立一個長度為 26 的計數器，代表 a-z
            count = [0] * 26
            for c in s:
                # 利用 ASCII 碼計算位移量，將字母對應到 0-25 的索引
                # e.g., 'a' -> 0, 'b' -> 1...
                count[ord(c) - ord('a')] += 1

            # Step 2-2: Add the element to the Map
            # 注意：在 Python 中 list 是可變的 (mutable)，不能當 Key，
            # 必須轉成不可變的 tuple 才能存入字典。
            
            res[tuple(count)].append(s)
        # Step3: Return Result
        return list(res.values())

        '''
        假設 strs = ["eat", "tea"]：

        當 s = "eat" 時：

        計算 count 特徵（a:1, e:1, t:1）。

        res[tuple(count)] 發現是空的，自動生出 []。

        .append("eat") → res 變成 {(1,0,0...): ["eat"]}。

        當 s = "tea" 時：

        計算 count 特徵（a:1, e:1, t:1） → 跟剛才一模一樣。

        res[tuple(count)] 直接指向剛才那個列表 ["eat"]。

        .append("tea") → res 變成 {(1,0,0...): ["eat", "tea"]}。
        '''