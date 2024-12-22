temperatures = [72, 68, 75, 70, 78, 74, 71]

highest_temperature = max(temperatures)
print("Highest temperature:", highest_temperature)

lowest_temperature = min(temperatures)
print("Lowest temperature:", lowest_temperature)

average_temperature = sum(temperatures) / len(temperatures)
print("Average temperature:", average_temperature)

above_70 = [temp for temp in temperatures if temp > 70]
print("Temperatures above 70:", above_70)
