class Solution:
    #Brute force
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n #initialise result array the same size as current one

        #For every element, calculate the product except for the current index
        for i in range(n): 
            prod = 1
            for j in range(n):
                if i == j:
                    continue    
                prod *= nums[j]
            
            res[i] = prod #append the result for that element to res
        return res
    
    # Division
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zero_cnt = 1, 0
        for num in nums:
            if num:
                prod *= num
            else:
                zero_cnt +=  1
        if zero_cnt > 1: return [0] * len(nums) #if two zeros are in the array, then the product will invariably be 0.

        res = [0] * len(nums)
        for i, c in enumerate(nums):
            if zero_cnt: res[i] = 0 if c else prod
            else: res[i] = prod // c
        return res
    
    #Prefix and suffix (optimal)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums)) #result array

        prefix = 1
        #prefix pass, gives you an array that has the total result before current index
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        #postfix pass, givess you the resulting array in total
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res