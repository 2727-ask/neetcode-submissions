class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        slow_time = 0
        cars = list(zip(position, speed))
        cars.sort(reverse=True)
        fleet = 0

        for distance, speed in cars:
            time  = (target - distance) / speed
            if(time > slow_time):
                fleet = fleet + 1 
                slow_time = time

        return fleet