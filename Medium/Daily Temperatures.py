# 739 - Daily Temperatures
# https://leetcode.com/problems/daily-temperatures

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answer = [0] * len(temperatures)
        s_temperatures = []

        for i in range(len(temperatures)):
            while s_temperatures and temperatures[s_temperatures[-1]] < temperatures[i]:
                last = s_temperatures.pop()
                answer[last] = i - last
            
            s_temperatures.append(i)

        return answer