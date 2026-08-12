class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        res = [1] * len(nums)
        prod = 1
        for i, num in enumerate(nums):
            res[i] = prod
            prod *= num
        

        prod = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] *= prod
            prod *= nums[i]
        
        return res