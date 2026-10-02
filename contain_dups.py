class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        m = set(nums)
        if len(m)<len(nums):
            return True
        else:
            return False