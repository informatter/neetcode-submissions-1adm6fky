class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        c=0
        for i in range(1,n):
            if nums[i] != nums[i-1]:
                c+=1
                nums[c]=nums[i]

        return c+1