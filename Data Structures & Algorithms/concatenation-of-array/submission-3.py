class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # 1
        # ans = []
        # for i in nums:
        #     ans.append(i)
        # for i in nums:
        #     ans.append(i)
        # return ans
        # 2
        ans = [0] * (2*len(nums))
        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[i+len(nums)] = nums[i]
        return ans