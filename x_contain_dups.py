class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        l = []
        sec = 1
        for i in range(0,len(nums)):
            count = 0
            if nums[i] == nums[sec]:
                