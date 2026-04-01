class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #思路： 記住我看過什麼，檢查字串某個元素是否出現過
        #題型：HashMap題型
        if len(s)!=len(t):
            return False
        # Step 1:  Initiate a map, store the key-value pair
        hashMapS = {}
        hashMapT = {}
        # Step 2:  Iterate over array
        for i in range(len(s)):
            #Step2-1: if element shows up before, do stuff
            #Step2-2: Add the element to the Map
            hashMapS[s[i]] =  hashMapS.get(s[i],0) +1
            hashMapT[t[i]] =  hashMapT.get(t[i],0) +1
        #Step2-3: 最終檢查
        return hashMapS == hashMapT





        