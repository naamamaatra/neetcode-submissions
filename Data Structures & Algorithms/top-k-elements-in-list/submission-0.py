from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the frequency of each number
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
            
        # Step 2: Create a bucket array where index = frequency
        # We need len(nums) + 1 to account for the max possible frequency
        freq = [[] for i in range(len(nums) + 1)]
        
        # Step 3: Populate the buckets
        for num, count_val in count.items():
            freq[count_val].append(num)
            
        # Step 4: Gather the top k elements by reading buckets backwards
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res