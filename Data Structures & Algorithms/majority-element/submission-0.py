class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = len(nums)//2 + 1
        for n in nums:
            c = nums.count(n)
            if c >= majority:
                return n