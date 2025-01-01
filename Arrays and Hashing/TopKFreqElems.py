# Approach 1: Count the frequency of each element, sort it and take the top k elements - O(nlogn)
# Approach 2: Use a maxheap and frequency as the key, pop the heap k times - O(klogn)
# Approach 3: Bucket sort
# Count the frequency of each element with a dict, group elements with the same frequency in buckets, then reverse traversal through those buckets to collect the k most frequent.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
         count = {}
         freq = [[] for i in range(len(nums) + 1)] # List of lists (buckets)
         
         for n in nums: #Count the frequency of each of each element
             count[n] = 1 + count.get(n, 0) # Increment element's frequency by 1 (default 0)
         for n, c in count.items(): # Group numbers by their frequencies (buckets)
             freq[c].append(n) # Add each number n to the bucket at index c (its frequency)
           
         #collect the top k freq elements    
         res = []
         for i in range(len(freq) - 1, 0, -1): # Starting from the highest frequency bucket, work backwards 
             #For each bucket (freq[i]) iterate through the numbers in the bucket, append each number to res, and stop when res contains k elements.
             for n in freq[i]: 
                 res.append(n) 
                 if len(res) == k:
                     return res
            