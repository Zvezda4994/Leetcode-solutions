class Solution:
    
    # Brute Force approach, compare every element with every other element, O(n^2)
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
    
    # Sort the array first then compare adjacent elements, O(n log n)
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                return True
            
        return False
    
    # Initialise a hash set and return true if we see an element thats already in the set
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
    
    # Make a set of nums and if it's smaller than nums (since sets only have unique elements) return true
    def hasDuplicate(self, nums: List[int]) -> bool:
        return (len(set(nums)) < len(nums))
            