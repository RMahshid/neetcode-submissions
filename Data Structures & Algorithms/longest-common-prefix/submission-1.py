class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #1
        # prefix = strs[0]

        # for s in strs[1:]:
        #     while not s.startswith(prefix):
        #         prefix = prefix[:-1]
        #     if prefix == "":
        #         return ""
        # return prefix
        # 2
        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res