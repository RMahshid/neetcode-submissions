class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1
        # anagram_map = {}
        # for word in strs:
        #     key = ''.join(sorted(word))
        #     if key not in anagram_map.keys():
        #         anagram_map[key]=[]
        #     anagram_map[key].append(word)
        # return list(anagram_map.values())
        # 2
        # anagram_map = defaultdict(list)
        # for word in strs:
        #     key = ''.join(sorted(word))
        #     anagram_map[key].append(word)
        # return list(anagram_map.values())
        #3
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c)-ord('a')] +=1
            res[tuple(count)].append(s)
        return list(res.values())
            