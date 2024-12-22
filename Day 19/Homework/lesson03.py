numbers = []

n = int(input("რამდენი რიცხვის შეყვანა გსურთ? "))

for i in range(n):
    num = int(input(f"შეიყვანეთ {i+1}-ე რიცხვი: "))
    numbers.append(num)

print("შექმნილი სია:", numbers)

reversed_list = []
for i in range(len(numbers) - 1, -1, -1):
    reversed_list.append(numbers[i])

print("სია საპირისპირო მიმდევრობით:", reversed_list)
