numbers = []

n = int(input("რამდენი რიცხვის შეყვანა გსურთ? "))

for i in range(n):
    num = int(input(f"შეიყვანეთ {i+1}-ე რიცხვი: "))
    numbers.append(num)

max_number = numbers[0]

for num in numbers:
    if num > max_number:
        max_number = num

print("უდიდესი რიცხვი სიაში არის:", max_number)
