class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # we have a list of nums, and we're looking for two that add up to target
        # which means for every num, we know what compliment were looking for: target-num

        comps = {}
        for index, num in enumerate(nums):
            if num in comps:
                return [comps[num], index]
            
            comps[target - num] = index