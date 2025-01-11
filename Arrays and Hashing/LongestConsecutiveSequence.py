class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #one solution is to sort and then iterate through finding the longest sequence (nlogn)
        #however the optimal solution would be to create a set, iterate through the array 
        #if an element doesn't have their left neighbour present in the set, it is the start of a sequence
        #calculate the length of each sequence by traversing through the entire array in one pass
        #This would be 0(n) in both time (one pass) and space (creating a set for the array)
        numSet = set(nums)
        longest = 0
        
        for n in nums:
            # Check if it's the start of a sequence
            if (n-1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
                