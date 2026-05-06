class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        output = False
        num_list = []
        for i in nums:
            for j in num_list:
                if i == j :
                    return True
            num_list.append(i)
        return output
        