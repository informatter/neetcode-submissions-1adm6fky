class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # create hashmap of each num -> will help identify sequence starts.
        # start iterating once sequence start is identified, 
        # a sequence is: i - 1 not in hashmap and i+1 in hashmap
        # keep track of sequences.

        # avoid double counting.
        # indentify start of sequence -> i-1
        # when start of sequence is identified, keep iterating until i +1 is in hashmap
        
        num_set = set(nums)
        max_sequence = 0

        for num in nums:
            
            # sequence start
            if num - 1 not in num_set:
                s = num
                c = 0
                while s in num_set:
                    s+=1
                    c+=1
                max_sequence = max(max_sequence,c)

        return max_sequence