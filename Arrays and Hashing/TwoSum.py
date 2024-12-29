class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevmap = {} # Initialise empty hashmap
        
        for i,n in enumerate(nums): #Iterate over index i and value n
            diff = target - n # Difference needed to reach the target at given index
            if diff in prevmap: # If difference is in the map, return both indices
                return [prevmap[diff], i]
            prevmap[n] = i # Otherwise add the current value to the map
        return