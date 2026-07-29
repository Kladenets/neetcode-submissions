class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # we have a list of nums, and we're looking for two that add up to target
        # which means for every num, we know what compliment were looking for: target-num

        comps = {}
        for i, n in enumerate(nums):
            if n in comps:
                return [comps[n], i]
            
            comps[target - n] = i