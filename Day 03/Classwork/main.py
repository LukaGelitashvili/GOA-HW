numbers = []

number_1 = int(input("Enter The First Number: "))
number_2 = int(input("Enter The Second Number: "))
number_3 = int(input("Enter The Third Number: "))
number_4 = int(input("Enter The Fourth Number: "))
number_5 = int(input("Enter The Fifth Number: "))

numbers.append(number_1)
numbers.append(number_2)
numbers.append(number_3)
numbers.append(number_4)
numbers.append(number_5)

print(numbers)
print(numbers[0],numbers[4])

print(numbers[0] * numbers[1])
print(numbers[2] / numbers[3])
print(numbers[3] + numbers[1])
print(numbers[4] - numbers[2])