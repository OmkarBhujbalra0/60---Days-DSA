class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        l = []
        
        for i in range(0,len(nums)):
            count = 1
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    count+=1
            l.append((nums[i],count))
    
        for i in l:
            if i[1]> int((len(nums)/2)):
                return i[0]

        