class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack=[]

        for current_day, temp in enumerate(temperatures):

            while stack and stack[-1][1] < temp:
                prev_day, prev_temp = stack.pop()
                result[prev_day] = current_day - prev_day
            stack.append((current_day,temp))
        return result
        