class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        res = [1] * len(nums)
        rProd, lProd = 1, 1
        for i in range(len(nums)):
            res[i] *= lProd
            lProd *= nums[i]
        
            rI = len(nums) - i - 1
            res[rI] *= rProd
            rProd *= nums[rI]
        
        return res