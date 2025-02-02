from typing import List

class Solution:
        def check(self, nums: List[int]) -> bool:
            numsOrdered = sorted(nums)
            
            for i in range(len(nums)):
                if numsOrdered[0] == nums[(0+i)%len(nums)]:
                    def orderPoint(nums, i):
                        return nums[(0+i)%len(nums):] + nums[:(0+i)%len(nums)]
                    if numsOrdered == orderPoint(nums, i):
                        return True
                    
            return False