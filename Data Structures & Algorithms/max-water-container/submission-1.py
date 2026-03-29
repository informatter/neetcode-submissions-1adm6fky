class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # base = e_p - s_p
        # height = min(heights[e_p],heights[s_p])
        # area = base*height
        # Return the max amount of water a container can store.

        # Heights can't be sorted
        # with what criteria are start pointer and end pointer updated?
        # move pointers towards largest height
        # if heights are equal move both pointers inwards
        # compute max area on every iteration

        sp,ep =0, len(heights)-1
        max_area = 0
        while sp < ep:
            base = ep - sp
            height = min(heights[ep],heights[sp])
            max_area = max(max_area,base*height)
            if heights[ep] < heights[sp]:
                ep-=1
            elif heights[ep] > heights[sp]:
                sp+=1
            else:
                ep-=1
                sp+=1
        return max_area

        # [1,7,2,5,4,7,3,6]

        