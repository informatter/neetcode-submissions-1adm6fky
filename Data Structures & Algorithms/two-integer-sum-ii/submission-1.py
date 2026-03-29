class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        s_p, e_p = 0, len(numbers)-1

        while s_p < e_p:
            s = numbers[s_p]+numbers[e_p]
            if s < target:
                s_p+=1
            elif s > target:
                e_p-=1
            else:
                return[s_p+1,e_p+1]
        return []


        