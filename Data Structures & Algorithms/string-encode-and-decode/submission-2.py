

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))

class Solution:
    def encode(self, strs: List[str]) -> str:
        #Step1-1:  初始化結果字串
        res =""
        #Step1-2:  For-Loop遍歷所有字串，建立特徵
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
        # 5#Hello5#World
    
    def decode(self, s: str) -> List[str]:
        #Step 2-1: 初始化結果與index
        res, i = [], 0
        #Step 2-2: while loop遍歷所有字串，拆解特徵,配合j指針
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            word = s[j+1: j+1 +length]
            res.append(word)
            i = j+1+length
        return res


        