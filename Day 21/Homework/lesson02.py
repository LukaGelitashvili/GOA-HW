numbers = list(range(1, 11))
print("Numbers list:", numbers)

first_half = numbers[:5]
print("First half:", first_half)

second_half = numbers[5:]
print("Second half:", second_half)

squares = [x**2 for x in numbers]
print("Squares of numbers:", squares)
