class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]== target:
        #             return [i,j]
        # return None
        # 2
        seen = {}
        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in seen:
                return [seen[needed],i]
            seen[nums[i]]=i