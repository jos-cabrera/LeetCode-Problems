# Problem 853 - Car Fleet
# https://leetcode.com/problems/car-fleet

class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # [pos, speed, time to target]
        cars = sorted((position[i], speed[i], (target - position[i]) / speed[i]) for i, pos in enumerate(position))

        fleets = [cars[len(cars) - 1]]

        for car in cars[-2::-1]:
            fleets.append(car)
            if fleets[-1][2] <= fleets[-2][2]:
                del fleets[-1]

        return len(fleets)