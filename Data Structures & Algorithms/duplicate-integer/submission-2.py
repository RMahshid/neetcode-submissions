class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # first idea
        # output = False
        # num_list = []
        # for i in nums:
        #     for j in num_list:
        #         if i == j :
        #             return True
        #     num_list.append(i)
        # return output

        # second idea
        # seen = set ()
        # for i in nums:
        #     if i in seen:
        #         return True
        #     seen.add(i)
        # return False

        #third idea
        return len(nums) != len(set(nums))