class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 1
        #return sorted(s) == sorted(t)
        # 2
        # if len(s) != len(t):
        #     return False
        # count_s = {}
        # count_t = {}
        # for ch in s:
        #     count_s[ch] = count_s.get(ch,0) + 1 
        # for ch in t:
        #     count_t[ch] = count_t.get(ch,0) + 1
        # return count_s == count_t
        # 3
        # if len(s) != len(t):
        #     return False
        # count = {}
        # for ch in s:
        #     count[ch] = count.get(ch,0)+1
        # for ch in t:
        #     count[ch] = count.get(ch,0)-1
        # for value in count.values():
        #     if value != 0:
        #         return False
        # return True
        # 4
        #return Counter(s) == Counter(t)
        # 5
        if len(s) != len(t):
            return False
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i],0)
        # one way : return countS == countT
        # secount way
        for c in countS:
            if countS[c] != countT.get(c,0):
                return False
        return True

