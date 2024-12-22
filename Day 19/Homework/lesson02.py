numbers = []

n = int(input("რამდენი რიცხვის შეყვანა გსურთ? "))

for i in range(n):
    num = int(input(f"შეიყვანეთ {i+1}-ე რიცხვი: "))
    numbers.append(num)

print("შექმნილი სია:", numbers)

element_to_remove = int(input("შეიყვანეთ რიცხვი, რომლის წაშლაც გსურთ: "))

if element_to_remove in numbers:
    numbers.remove(element_to_remove)
    print("განახლებული სია:", numbers)
else:
    print("შეყვანილი ელემენტი სიაში არ არსებობს.")
