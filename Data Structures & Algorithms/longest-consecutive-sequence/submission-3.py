class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # create hashmap of each num -> will help identify sequence starts.
        # start iterating once sequence start is identified, 
        # a sequence is: i - 1 not in hashmap
        # keep track of sequences.

        # indentify start of sequence -> i-1
        # when start of sequence is identified, keep iterating until i +1 is in hashmap
        
        num_set = set(nums)
        max_sequence = 0

        for num in num_set:
            
            # if num - 1  in num_set:
            #     continue
            # sequence start
            curr = num
            lenght = 1
            while curr + 1 in num_set:
                curr+=1
                lenght+=1
            max_sequence = max(max_sequence,lenght)

        return max_sequence