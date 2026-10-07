class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        product = 1
        for i in range(len(nums)):
            if i > 0:
                product *= nums[i-1]
            prefix[i] = product
        
        product = 1
        for j in range(len(nums) - 1, -1, -1):
            if j < len(nums) - 1:
                product *= nums[j+1]
            suffix[j] = product

        return list(map(lambda e : e[0] * e[1], zip(prefix, suffix)))