sum_even = 0
count_even = 0
number = 1

while number <= 100:
    if number % 2 == 0:
        sum_even += number
        count_even += 1
    number += 1

average = sum_even / count_even

print("1-დან 100-მდე ყველა ლუწი რიცხვის საშუალო არითმეტიკულია:", average)
