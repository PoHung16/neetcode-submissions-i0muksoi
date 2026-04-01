class Solution:
    def encode(self, strs: List[str]) -> str:
        # Step 1: 初始化結果字串
        res = ""
        # Step 2: 遍歷所有字串，建立特徵
        for s in strs:
            # 格式：長度 + 分隔符 + 字串本身
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        # Step 1: 初始化結果列表與指標
        res, i = [], 0
        
        # Step 2: 遍歷長字串
        while i < len(s):
            # Step 2-1: 尋找分隔符 #，確定長度的終點
            j = i
            while s[j] != "#":
                j += 1
            
            # Step 2-2: 提取長度（從 i 到 j 是數字, j是分隔符）
            length = int(s[i:j])
            
            # Step 2-3: 根據長度切片提取原始字串內容
            # 字串開始位置在 j + 1，結束位置在 j + 1 + length
            word = s[j + 1 : j + 1 + length]
            res.append(word)
            
            # Step 2-4: 指標跳轉到下一個字串的起點 ,上一串字串得終點
            i = j + 1 + length
            
        return res


