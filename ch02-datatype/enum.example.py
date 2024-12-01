from enum import Enum


class TrafficLight(Enum):
    GREEN = 1
    YELLOW = 2
    RED = 3


print(TrafficLight.GREEN)  # TrafficLight.GREEN
print(TrafficLight.GREEN.name)  # GREEN
print(TrafficLight.GREEN.value)  # 1

print(TrafficLight(1))  # TrafficLight.GREEN
print(TrafficLight(3))  # TrafficLight.RED
