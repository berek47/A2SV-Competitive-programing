class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        chara = strs[0] #flower
        for c in strs[1:]:#flow , flight
            while c[:len(chara)] != chara: # c[0:lens(flower)] = c[0:6] = flow != flower ==> flig != flow 
                print(c) #flow
                chara = chara[:-1] #flowe , flow ==>  (flow == flow) ==> fli , fl ==> (fl == fl)
                print(c)
                if not chara:
                    return ""
        return chara
